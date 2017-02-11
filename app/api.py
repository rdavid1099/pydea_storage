from datetime import datetime

class Api(object):
    @classmethod
    def get_all_ideas(self, models):
        ideas = models.Idea.query.all()
        idea_format = []
        for idea in ideas:
            format_idea = {}
            format_idea['id'] = idea.id
            format_idea['title'] = idea.title
            format_idea['description'] = idea.description
            format_idea['uid'] = idea.uid
            format_idea['timestamp'] = idea.timestamp
            format_idea['category'] = models.Category.query.get(idea.category_id).name
            idea_format.append(format_idea)
        return idea_format

    @classmethod
    def get_idea(self, idea_id, models):
        idea = models.Idea.query.get(idea_id)
        if idea == None:
            return False
        else:
            return self.idea_hash(idea, models)

    @classmethod
    def create_idea(self, params):
        raw_idea = {
        'title': params.get('title'),
        'description': params.get('description'),
        'uid': params.get('uid'),
        'timestamp': datetime.utcnow(),
        'category_id': params.get('category')
        }
        if raw_idea['title'] == None or raw_idea['description'] == None or raw_idea['uid'] == None:
            return False
        else:
            return raw_idea

    @classmethod
    def save_idea(self, new_idea, models, db):
        idea = models.Idea(
        title=new_idea['title'],
        description=new_idea['description'],
        uid=new_idea['uid'],
        timestamp=new_idea['timestamp'],
        category_id=new_idea['category_id']
        )
        db.session.add(idea)
        db.session.commit()

    @classmethod
    def update_idea(self, params, idea_id, models, db):
        idea = models.Idea.query.get(idea_id)
        if idea == None:
            return False
        else:
            idea.title = params.get('title') or idea.title
            idea.description = params.get('description') or idea.description
            idea.timestamp = datetime.utcnow()
            idea.category_id = params.get('category') or idea.category_id
            db.session.commit()
            return self.idea_hash(idea, models)

    @classmethod
    def delete_idea(self, idea_id, models, db):
        idea = models.Idea.query.get(idea_id)
        if idea == None:
            return False
        else:
            db.session.delete(idea)
            db.session.commit()
            return True

    @classmethod
    def idea_hash(self, idea, models):
        return {
        'id': idea.id,
        'title': idea.title,
        'description': idea.description,
        'uid': idea.uid,
        'timestamp': idea.timestamp,
        'category': models.Category.query.get(idea.category_id).name
        }
