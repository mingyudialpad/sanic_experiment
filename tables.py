import sqlalchemy


metadata = sqlalchemy.MetaData()

pricing = sqlalchemy.Table(
    'licenses',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('lite_lines', sqlalchemy.String(length=10)),
    sqlalchemy.Column('agents', sqlalchemy.String(length=10)),
    sqlalchemy.Column('magenta_lines', sqlalchemy.String(length=10)),
    sqlalchemy.Column('tollfree_room_lines', sqlalchemy.String(length=10)),
    sqlalchemy.Column('group_lines', sqlalchemy.String(length=10)),
    sqlalchemy.Column('tollfree_group_lines', sqlalchemy.String(length=10)),
    sqlalchemy.Column('fax_lines', sqlalchemy.String(length=10)),
    sqlalchemy.Column('uc_tier_1', sqlalchemy.String(length=10)),
    sqlalchemy.Column('uc_tollfree_tier_1', sqlalchemy.String(length=10)),
    sqlalchemy.Column('tollfree_tier_b', sqlalchemy.String(length=10)),
    sqlalchemy.Column('tollfree_tier_c', sqlalchemy.String(length=10)),
    sqlalchemy.Column('tollfree_tier_d', sqlalchemy.String(length=10)),
    sqlalchemy.Column('local_presence_top100', sqlalchemy.String(length=10)),
    sqlalchemy.Column('local_presence_all', sqlalchemy.String(length=10)),
)