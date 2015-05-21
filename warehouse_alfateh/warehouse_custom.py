from openerp import models,  fields,  api
class stock_picking(models.Model):
    _inherit = "stock.picking"
    customer_ntn = fields.Char(string="Customer NTN" )
    customer_cnic = fields.Char(string="Customer CNIC" )
    supplier_ntn = fields.Char(string="Supplier NTN" )
    supplier_cnic = fields.Char(string="Supplier CNIC" )
    buyer_type = fields.Selection([('registered','Registered'), ('unregistered','Unregistered'),('bulk_unregistered','Bulk-Unregistered'),('retail_customer','Retail Consumers')],"Buyer Type" )
    province = fields.Selection([('punjab','Punjab'), ('sindh','Sindh'),('balochistan','Balochistan'),('kpk','KPK')],"Province" )
    invoice_state = fields.Selection(default='2binvoiced')
    
    @api.onchange('partner_id')
    def update_fields(self):
        self.customer_ntn = self.partner_id.customer_ntn
        self.customer_cnic = self.partner_id.customer_cnic
        self.supplier_ntn = self.partner_id.supplier_ntn
        self.supplier_cnic = self.partner_id.supplier_cnic
        self.buyer_type = self.partner_id.buyer_type
        self.province = self.partner_id.province