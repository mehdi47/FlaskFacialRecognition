from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Ads
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, FileField, validators
from passlib.hash import sha256_crypt
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_wtf.file import FileField, FileAllowed, FileRequired
import os

app = Flask(__name__)

# Uploads
UPLOADS_DEFAULT_DEST = '/img/'
UPLOADS_DEFAULT_URL = 'http://localhost:5000/img'

UPLOADED_FILES_DEST = '/img'
UPLOADED_FILES_URL = 'http://localhost:5000/img'

# Configure the image uploading via Flask-Uploads
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = UPLOADED_FILES_DEST
# app.config['UPLOADED_DEFAULT_DEST'] = UPLOADS_DEFAULT_DEST
# app.config['UPLOADED_PHOTOS_URL'] = UPLOADED_FILES_URL
# app.config['UPLOADED_DEFAULT_URL'] = UPLOADS_DEFAULT_URL
configure_uploads(app, photos)
patch_request_class(app , 32 * 1024 * 1024)

# Config MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pfa'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

Ads = Ads()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/testt')
# def about2():
#     return render_template('test.html')

@app.route('/ads')
def ads():
    return render_template('ads.html', ads=Ads)

@app.route('/ad/<string:id>/')
def ad(id):
    return render_template('ad.html', id=id)

class RegisterForm(Form):
    firstname = StringField('FirstName', [validators.length(min=1,max=50)])
    lastname = StringField('LastName', [validators.length(min=1,max=50)])
    username = StringField('Username', [validators.length(min=4, max=25)])
    email = StringField('Email', [validators.length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm',message='passwords do not match')
    ])
    confirm = PasswordField('confirm password')
    photo = FileField('Photo', validators=[FileAllowed(photos, 'Images only!')])

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        file = request.files['photo']
        filename = file.filename
        file.save(os.path.join('img', filename))
        file_url = photos.url(filename)

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute Query
        cur.execute(("insert into user(nom,prenom,email,username,password) values('%s','%s','%s','%s','%s')")%(firstname,lastname,email,username,password))

        # Commit to DB
        mysql.connection.commit()

        cur.close()

        flash('you are now registered and can log in','success')

        return redirect(url_for('index'))

    return render_template('register.html', form=form)


class RegisterForm2(Form):
    cvname = StringField('CV Name:', [validators.optional(), validators.length(min=1,max=100)])
    name = StringField('Full Name:', [validators.required(), validators.length(min=1,max=100)])
    email = StringField('E-Mail:', [validators.required(), validators.length(min=1,max=100)])
    contact = StringField('Contact:', [validators.required(), validators.length(min=1,max=100)])
    fathername = StringField('Father Name:', [validators.optional(), validators.length(min=1,max=100)])
    address = StringField('Complete Address:', [validators.required(), validators.length(min=1,max=100)])
    residance = StringField('Residance Contact:', [validators.required(), validators.length(min=1,max=100)])
    dob = StringField('Date Of Birth:', [validators.required(), validators.length(min=1,max=100)])
    lang = StringField('Languages known:', [validators.required(), validators.length(min=1,max=100)])
    gb = StringField('Graduation College name:', [validators.required(), validators.length(min=1,max=100)])
    gm = StringField('Graduation subjects or stream:', [validators.required(), validators.length(min=1,max=100)])
    gp = StringField('Graduation passing year:', [validators.required(), validators.length(min=1,max=100)])
    gs = StringField('Graduation marks :', [validators.required(), validators.length(min=1,max=100)])

    tb = StringField('10th BOARD name:', [validators.required(), validators.length(min=1,max=100)])
    tm = StringField('10th subjects:', [validators.required(), validators.length(min=1,max=100)])
    tp = StringField('10th passing year:', [validators.required(), validators.length(min=1,max=100)])
    ts = StringField('10th marks :', [validators.required(), validators.length(min=1,max=100)])
    tvb = StringField('12th BOARD name::', [validators.required(), validators.length(min=1,max=100)])
    tvm = StringField('12th stream:', [validators.required(), validators.length(min=1,max=100)])
    tvp = StringField('12th passing year:', [validators.required(), validators.length(min=1,max=100)])
    tvs = StringField('12th marks :', [validators.required(), validators.length(min=1,max=100)])

    projetcs = TextAreaField('Your projetcs in detail:', [validators.required(), validators.length(min=1,max=1000)])
    skills = TextAreaField('Your Skills:', [validators.required(), validators.length(min=1,max=1000)])
    achievements = TextAreaField('Your achievements:', [validators.required(), validators.length(min=1,max=1000)])


@app.route('/hindicv', methods=['GET','POST'])
def select():
    form = RegisterForm2(request.form)
    if request.method == 'POST' and form.validate():
        cvname = form.cvname.data
        name = form.name.data
        email = form.email.data
        contact = form.contact.data
        fathername = form.fathername.data
        address = form.address.data
        residance = form.residance.data
        dob = form.dob.data
        lang = form.lang.data
        gb = form.gb.data
        gm = form.gm.data
        gp = form.gp.data
        gs = form.gs.data

        tb = form.tb.data
        tm = form.tm.data
        tp = form.tp.data
        ts = form.ts.data
        tvb = form.tvb.data
        tvm = form.tvm.data
        tvp = form.tvp.data
        tvs = form.tvs.data

        projetcs = form.projetcs.data
        skills = form.skills.data
        achievements = form.achievements.data

        # Create Cursor
        cur = mysql.connection.cursor()
        curr = mysql.connection.cursor()
        # Execute Query
        cur.execute(("insert into cv_hindi(cv_name,user_fullname,user_email,user_contact,user_address,user_residance,user_birthdate,user_languages,user_gcollege,user_gsubjects,user_gyear,user_gmark,user_tnboard,user_tnsubject,user_tnpassyear,user_tnmark,user_twboard,user_twstream,user_twpassyear,user_twmark,user_projects,user_skills,user_achievements) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')")%(cvname, name, email, contact,  address, residance, dob, lang, gb, gm, gp, gs, tb, ts, tp, tm, tvb, tvs, tvp, tvm, projetcs, skills, achievements))
        curr.execute(("insert into user(cv_name) values('%s')")%(cvname))
        # Commit to DB
        mysql.connection.commit()


        cur.close()
        curr.close()
        flash('you are now registered and can log in', 'success')

        return render_template('cv.html', cvname = cvname, name = name, email = email, contact = contact, dob = dob, lang = lang, address = address,
                                    fathername=fathername, residance=residance, gp=gp, gs=gs, gm=gm, gb=gb, tb=tb, tp=tp, tm=tm,
                                    ts=ts, tvb=tvb, tvm=tvm, tvp=tvp, tvs=tvs, projetcs=projetcs, skills=skills,
                                    achievements=achievements)

    return render_template('hindicv.html', cvname=form.cvname.data, name=form.name.data, email=form.email.data,
                           contact=form.contact.data, dob=form.address.data, lang=form.lang.data,address=form.address.data,
                           fathername=form.fathername.data, residance=form.residance.data,
                           gp=form.gp.data, gs=form.gs.data, gm=form.gm.data, gb=form.gb.data, tb=form.tb.data, tp=form.tp.data,
                           tm=form.tm.data, ts=form.ts.data, tvb=form.tvb.data, tvm=form.tvm.data,
                           tvp=form.tvp.data, tvs=form.tvs.data, projetcs=form.projetcs.data, skills=form.skills.data,
                           achievements=form.achievements.data, form=form)


# @app.route('/hello/', methods=['GET','POST'])
# def hello():
#     form = RegisterForm2(request.form)
#     if request.method == 'POST' and form.validate():
#         cvname = form.cvname.data
#         name = form.name.data
#         email = form.email.data
#         contact = form.contact.data
#         fathername = form.fathername.data
#         address = form.address.data
#         residance = form.residance.data
#         dob = form.dob.data
#         lang = form.lang.data
#         gb = form.gb.data
#         gm = form.gm.data
#         gp = form.gp.data
#         gs = form.gs.data
#
#         tb = form.tb.data
#         tm = form.tm.data
#         tp = form.tp.data
#         ts = form.ts.data
#         tvb = form.tvb.data
#         tvm = form.tvm.data
#         tvp = form.tvp.data
#         tvs = form.tvs.data
#
#         projetcs = form.projetcs.data
#         skills = form.skills.data
#         achievements = form.achievements.data
#
#     return render_template('cv.html', cvname=cvname, name=name, email=email, contact=contact, dob=dob, lang=lang, address=address,
#                            fathername=fathername, residance=residance, gp=gp, gs=gs, gm=gm, gb=gb, tb=tb, tp=tp, tm=tm,
#                            ts=ts, tvb=tvb, tvm=tvm, tvp=tvp, tvs=tvs, projetcs=projetcs, skills=skills,
#                            achievements=achievements)


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
