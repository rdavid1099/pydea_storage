from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
category = Table('category', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
)

idea = Table('idea', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=64)),
    Column('description', VARCHAR(length=120)),
    Column('uid', INTEGER),
    Column('category', VARCHAR(length=64)),
)

idea = Table('idea', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('description', String(length=120)),
    Column('uid', Integer),
    Column('timestamp', DateTime),
    Column('category_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['category'].create()
    pre_meta.tables['idea'].columns['category'].drop()
    post_meta.tables['idea'].columns['category_id'].create()
    post_meta.tables['idea'].columns['timestamp'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['category'].drop()
    pre_meta.tables['idea'].columns['category'].create()
    post_meta.tables['idea'].columns['category_id'].drop()
    post_meta.tables['idea'].columns['timestamp'].drop()
