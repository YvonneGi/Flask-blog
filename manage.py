from flaskblog import app
# from  flask_migrate import Migrate, MigrateCommand


# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True)