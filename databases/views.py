from flask import render_template, request

from models import Person

def register_routes(app, db):

    @app.route(rule='/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template(
                template_name_or_list='index.html',
                people=people
            )
        elif request.method == 'POST':
            name=request.form.get('name')
            age=int(request.form.get('age'))
            job=request.form.get('job')

            person = Person(name=name, age=age, job=job)

            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template(
                template_name_or_list='index.html',
                people=people
            )

    @app.route(rule='/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()

        db.session.commit()

        people = Person.query.all()

        return render_template(
            template_name_or_list='index.html',
            people=people
        )

    @app.route(rule='/details/<pid>')
    def details(pid):
        person = Person.query.filter(Person.pid == pid).first()

        return render_template(template_name_or_list='details.html', person=person)
