from boxoffice.models import db, BaseNameMixin
from boxoffice.models.user import Organization
from boxoffice.models.category import Category
from boxoffice.models.event import event_item
from boxoffice.models.discount_policy import item_discount_policy

__all__ = ['Item']


class Item(BaseNameMixin, db.Model):
    """
    An item is a single type of inventory
    """
    __tablename__ = 'item'
    __uuid_primary_key__ = True

    description = db.Column(db.Unicode(2500), default=u'', nullable=True)

    organization_id = db.Column(None, db.ForeignKey('organization.id'), nullable=False)
    organization = db.relationship(Organization,
        backref=db.backref('items', cascade='all, delete-orphan'))

    category_id = db.Column(None, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship(Category, primaryjoin=category_id == Category.id)

    quantity_available = db.Column(db.Integer, default=0, nullable=False)
    quantity_total = db.Column(db.Integer, default=0, nullable=False)

    events = db.relationship('Event', secondary=event_item)
    discount_policies = db.relationship('DiscountPolicy', secondary=item_discount_policy)
    # TODO add check constraint quantity_available <= quantity_total

    def __repr__(self):
        return u'<Item "{item}">'.format(item=self.title)
