from db import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=False)
    is_vendor = db.Column(db.Boolean, default=False)
    dob = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    # Address Fields
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip = db.Column(db.String(20), nullable=False)

    # Contact Fields
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    # Financial Info Fields
    bank_account_number = db.Column(db.String(50), nullable=False)
    bank_branch = db.Column(db.String(100), nullable=False)
    ifsc_code = db.Column(db.String(20), nullable=False)
    credit_card_number = db.Column(db.String(50), nullable=False)
    credit_card_expiry = db.Column(db.String(20), nullable=False)
    credit_card_cvv = db.Column(db.String(5), nullable=False)
    income = db.Column(db.String(50), nullable=False)

    # Purchase History Fields
    order_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.String(50), nullable=False)
    transaction_amount = db.Column(db.String(50), nullable=False)

    # Preferences Fields
    product_preferences = db.Column(db.Text, nullable=False)
    communication_channels = db.Column(db.Text, nullable=False)
    feedback_given = db.Column(db.Boolean, nullable=False)

    # Interactions Fields
    customer_service_calls = db.Column(db.Integer, nullable=False)
    complaints_raised = db.Column(db.Integer, nullable=False)

    # Social Media Fields
    facebook_profile = db.Column(db.String(100), nullable=True)
    twitter_profile = db.Column(db.String(100), nullable=True)
    posts_liked = db.Column(db.Integer, nullable=False)
    comments_posted = db.Column(db.Integer, nullable=False)

    # Demographic Info Fields
    age_group = db.Column(db.String(50), nullable=False)
    marital_status = db.Column(db.String(50), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)

    def __init__(self, name, created_at, image, status, is_vendor, dob, gender, street, city, state, zip,
                 phone, email, bank_account_number, bank_branch, ifsc_code, credit_card_number, credit_card_expiry,
                 credit_card_cvv, income, order_id, product_id, purchase_date, transaction_amount, product_preferences,
                 communication_channels, feedback_given, customer_service_calls, complaints_raised, facebook_profile,
                 twitter_profile, posts_liked, comments_posted, age_group, marital_status, occupation):
        self.name = name
        self.created_at = created_at
        self.image = image
        self.status = status
        self.is_vendor = is_vendor
        self.dob = dob
        self.gender = gender
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email
        self.bank_account_number = bank_account_number
        self.bank_branch = bank_branch
        self.ifsc_code = ifsc_code
        self.credit_card_number = credit_card_number
        self.credit_card_expiry = credit_card_expiry
        self.credit_card_cvv = credit_card_cvv
        self.income = income
        self.order_id = order_id
        self.product_id = product_id
        self.purchase_date = purchase_date
        self.transaction_amount = transaction_amount
        self.product_preferences = product_preferences
        self.communication_channels = communication_channels
        self.feedback_given = feedback_given
        self.customer_service_calls = customer_service_calls
        self.complaints_raised = complaints_raised
        self.facebook_profile = facebook_profile
        self.twitter_profile = twitter_profile
        self.posts_liked = posts_liked
        self.comments_posted = comments_posted
        self.age_group = age_group
        self.marital_status = marital_status
        self.occupation = occupation

    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.name}', created_at='{self.created_at}', status='{self.status}', " \
               f"is_vendor={self.is_vendor}, dob='{self.dob}', gender='{self.gender}')"
