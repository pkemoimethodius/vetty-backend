"""Flattened customer model

Revision ID: 96b48b5328ec
Revises: 
Create Date: 2024-11-18 18:56:47.605270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96b48b5328ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('is_vendor', sa.Boolean(), nullable=True),
    sa.Column('dob', sa.String(length=10), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('street', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('state', sa.String(length=100), nullable=False),
    sa.Column('zip', sa.String(length=20), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('bank_account_number', sa.String(length=50), nullable=False),
    sa.Column('bank_branch', sa.String(length=100), nullable=False),
    sa.Column('ifsc_code', sa.String(length=20), nullable=False),
    sa.Column('credit_card_number', sa.String(length=50), nullable=False),
    sa.Column('credit_card_expiry', sa.String(length=20), nullable=False),
    sa.Column('credit_card_cvv', sa.String(length=5), nullable=False),
    sa.Column('income', sa.String(length=50), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('purchase_date', sa.String(length=50), nullable=False),
    sa.Column('transaction_amount', sa.String(length=50), nullable=False),
    sa.Column('product_preferences', sa.Text(), nullable=False),
    sa.Column('communication_channels', sa.Text(), nullable=False),
    sa.Column('feedback_given', sa.Boolean(), nullable=False),
    sa.Column('customer_service_calls', sa.Integer(), nullable=False),
    sa.Column('complaints_raised', sa.Integer(), nullable=False),
    sa.Column('facebook_profile', sa.String(length=100), nullable=True),
    sa.Column('twitter_profile', sa.String(length=100), nullable=True),
    sa.Column('posts_liked', sa.Integer(), nullable=False),
    sa.Column('comments_posted', sa.Integer(), nullable=False),
    sa.Column('age_group', sa.String(length=50), nullable=False),
    sa.Column('marital_status', sa.String(length=50), nullable=False),
    sa.Column('occupation', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    # ### end Alembic commands ###