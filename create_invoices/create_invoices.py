from openerp import models, fields, api
class create_invoice(models.Model):
    _inherit = "account.invoice"
    
    @api.model
    def create_students_invoices(self):
        students = self.env['res.partner'].search([('customer', '=', True)])
        
        
        for partner_id in students:
            account_id = False
            payment_term_id = False
            fiscal_position = False
            bank_id = False
            
            if partner_id:
                p = self.env['res.partner'].browse(partner_id)
                rec_account = p.property_account_receivable
                pay_account = p.property_account_payable
                
                if type in ('out_invoice', 'out_refund'):
                    account_id = rec_account.id
                    payment_term_id = p.property_payment_term.id
                else:
                    account_id = pay_account.id
                    payment_term_id = p.property_supplier_payment_term.id
                fiscal_position = p.property_account_position.id
                bank_id = p.bank_ids and p.bank_ids[0].id or False
            
            invoice = {
                'partner_id':partner_id,
                'account_id':account_id,
                'fiscal_position':fiscal_position
            }
            # creating invoices
            invoice_id = self.env['account.invoice'].create(invoice).id
            
            product = self.pool.get('product.product').search()[0]
            result = {
                'name': product.name,
                'account_id': account_id,
                'product_id': product.id,
                'invoice_id':invoice_id
            }
            
            invoice_line_id = self.env['account.invoice.line'].create(result).id
            return invoice_line_id