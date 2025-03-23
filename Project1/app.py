from flask import  Flask ,render_template,session,request,redirect ,url_for # package initilization
from flask_sqlalchemy import SQLAlchemy # flask sql alchemy initilization
from flask_uploads import uploaded_file,IMAGES,UploadSet
from flask_migrate import Migrate
from flask_mail import  Mail, Message
def create_app():
    app = Flask(__name__,template_folder="templates") # app initiliztion
    app.config['DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI']='SQLITE:///db.sqlite '
    app.config['UPLOAD_PHOTO_DEST']='/pictures'
    # app.config.from_file('config.cfg')
    #email config only
    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = 'balan.kamatchi92@gmail.com'  # Replace with your email
    # app.config['MAIL_PASSWORD'] = 'ptjabwzqikrjrilr'  # Use an app password if using Gmail
    # app.config['MAIL_DEFAULT_SENDER'] ='balan.kamatchi92@gmail.com' # Defau

    db = SQLAlchemy(app)
    migrate = Migrate()
    mail = Mail()
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    # class Test (db.Model):
    #     id = db.Column(db.Integer ,primary_key=True)
    @app.route("/") # default route
    def index():
        return "hello flask"
    @app.route("/email") # default route
    def emailsend():
        try:
            msg = Message(
                subject="Hello from Flask",
                recipients=["softbala92@gmail.com"],  # Replace with recipient email
                body="This is a test email sent from Flask!"
            )
            mail.send(msg)
            return "Mail Sent Successfully!"
        except Exception as e:
            return f"Error: {e}"
    @app.route("/upload",method=['GET','POST'])
    def uploads():
        return render_template('upload.html')
    return app
if __name__=="__main__":
    app.run()
