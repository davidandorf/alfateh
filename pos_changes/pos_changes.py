from openerp import models, fields, api
class product_custom_ean(models.Model):
    _inherit = "product.product"

    def _check_ean_key(self, cr, uid, ids, context=None):
    	return true;

class packaging_custom_ean(models.Model):
    _inherit = "product.packaging"

    def _check_ean_key(self, cr, uid, ids, context=None):
    	return true;

    