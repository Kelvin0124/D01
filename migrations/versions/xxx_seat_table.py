"""seat table

Revision ID: xxx
Revises: 
Create Date: 2023-4-19 02:17:42.131626

"""
from alembic import op
import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

# revision identifiers, used by Alembic.
revision = 'xxx'
down_revision = None
branch_labels = None
depends_on = None



db = SQLAlchemy()

class Seat(db.Model):
    __tablename__ = 'seat'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    seat_number = db.Column(db.Integer)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'))

    def __repr__(self):
        return '<Seat %r>' % self.id

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
)
    

    op.create_table('seat',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('room_id', sa.Integer(), nullable=True),
        sa.Column('seat_number', sa.Integer(), nullable=True),
        sa.Column('booking_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['booking_id'], ['booking.id'], ),
        sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
