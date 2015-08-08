from openerp import models, fields, api
class custom_invoice(models.Model):
    _inherit = "account.invoice"
    customer_ntn = fields.Char(string="Customer NTN" )
    customer_cnic = fields.Char(string="Customer CNIC" )
    supplier_ntn = fields.Char(string="Supplier NTN" )
    supplier_cnic = fields.Char(string="Supplier CNIC" )
    buyer_type = fields.Selection([('registered','Registered'), ('unregistered','Unregistered'),('bulk_unregistered','Bulk-Unregistered'),('retail_customer','Retail Consumers')],"Buyer Type" )
    province = fields.Selection([('punjab','Punjab'), ('sindh','Sindh'),('balochistan','Balochistan'),('kpk','KPK')],"Province" )
    
    
    @api.multi
    def onchange_partner_id(self, type, partner_id, date_invoice=False,payment_term=False, partner_bank_id=False, company_id=False):
        p = self.env['res.partner'].browse(partner_id)
        
        prev_result = super(custom_invoice,self).onchange_partner_id(type, partner_id, date_invoice,payment_term, partner_bank_id, company_id)
        added_result = prev_result['value']
        added_result['customer_ntn'] = p.customer_ntn
        added_result['customer_cnic'] = p.customer_cnic
        added_result['supplier_ntn'] = p.supplier_ntn
        added_result['buyer_type'] = p.buyer_type
        added_result['supplier_cnic'] = p.supplier_cnic
        added_result['province'] = p.province
        print(added_result)
        return {'value': added_result}
    
    
    
class custom_invoice_line(models.Model):
    _inherit = "account.invoice.line"
    sale_type = fields.Selection([('1', 'Goods at standard rate'),  ('2', 'Third Schedule Goods'), ('3', 'Good at Reduced Rate'), ('4', 'Electricity Supply to Retailers'), ('5', 'Electricity to stell sector'), ('6', 'Gas to CNG stations'), ('7', 'Re-rollable scrap by ship-breakers'), ('8', 'SIM sale / IMEI activation')], "Sale Type")
    schedule_no = fields.Selection([('1', '(549(I)/2008'),  ('2', '811(I)/2009'), ('3', 'Zero Rated Elec.'), ('4', 'Zero Rated Gas'), ('5', '5th Schedule'), ('6', '1125(I)/2011'), ('7', '608(I)/2012'), ('8', '79(I)/2012'), ('9', '1st Schedule FED'), ('10', '1007(I)/2005'), ('11', '326(I)/2008'), ('12', '539(I)/2008'), ('13', '542(I)/2008'), ('14', '551(I)/2008'), ('15', '727(I)/2011'), ('16', '76(I)/2008'), ('17', '880(I)/2007'), ('18', '6th Schd Table I'), ('19', '6th Schd Table II'), ('20', 'DTRE'), ('21', 'FED 3rd Schd Table I'), ('22', 'FED 3rd Schd Table II'), ('23', 'Section 4(b)'), ('24', '802(I)/2009'), ('25', '678(I)/2004'), ('26', '760(I)/2012'), ('27', '213(I)/2013'), ('28', '499(I)/2013'), ('29', '501(I)/2013'), ('30', '670(I)/2013'), ('31', '657(I)/2013'), ('32', '898(I)/2013'), ('33', '896(I)/2013'), ('34', '460(I)/2013')], "SRO No. / Schedule No.")
    item_sr_no = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48'),('49','49'),('50','50'),('51','51'),('52','52'),('53','53'),('54','54'),('55','55'),('56','56'),('57','57'),('58','58'),('59','59'),('60','60'),('61','61'),('62','62'),('63','63'),('64','64'),('65','65'),('66','66'),('67','67'),('68','68'),('69','69'),('70','70'),('71','71'),('72','72'),('73','73'),('74','74'),('75','75'),('76','76'),('77','77'),('78','78'),('79','79'),('80','80'),('81','81'),('82','82'),('83','83'),('84','84'),('85','85'),('86','86'),('87','87'),('88','88'),('89','89'),('90','90'),('91','91'),('92','92'),('93','93'),('94','94'),('95','95'),('96','96'),('97','97'),('98','98'),('99','99'),('100','100'),('101','101'),('102','102'),('103','103'),('104','104'),('105','105'),('106','106'),('107','107'),('108','108'),('109','109'),('110','110'),('111','111'),('112','112'),('113','113'),('114','114'),('115','115'),('116','116'),('117','117'),('118','118'),('119','119'),('120','120'),('121','121'),('122','122'),('123','123'),('124','124'),('125','125'),('126','126'),('127','127'),('128','128'),('129','A'),('130','B'),('131','C'),('132','52A')], "Item Sr. No.")
    doc_type = fields.Selection([('0','SI'), ('1','STWH')],"Document Type" )
    x_quantity = fields.Float(string="Quantity" )
    x_uom = fields.Float(string="UOM" )
    x_extra_tax = fields.Float(string="Extra Tax" )
    x_st_withheld = fields.Float(string="ST Withheld at source" )
    x_further_tax = fields.Float(string="Further tax" )
    x_rate = fields.Selection([('1', '17'),  ('2', '2'), ('3', '3'), ('4', '5'), ('5', '7.5'), ('6', '8'), ('7', '10'), ('8', '16'), ('9', '18.5'), ('10', '0'), ('11', '0.5'), ('12', 'Exempt'), ('13', 'DTRE'), ('14', 'Rs.7/KWH'), ('15', '6700-MT'), ('16', 'Rs.1/kg'), ('17', 'Rs. 8/KWH'), ('18', 'Rs. 250/SIM'), ('19', 'Rs.500/IMEI'), ('20', 'Rs.250/IMEI'),('21', 'Rs.150/IMEI'),('22', '22'),('23', '27'),('24', '18'),('25', '32'),('26', '37')], "Rate")
    x_hs_code = fields.Float(string="HS Code")
    item_seller_price = fields.Float(string="Seller Price")
    
    @api.multi
    def product_id_change(self, product, uom_id, qty=0, name='', type='out_invoice',partner_id=False, fposition_id=False, price_unit=False, currency_id=False,company_id=None):
        p = self.env['product.product'].browse(product)
        
        prev_result = super(custom_invoice_line,self).product_id_change(product, uom_id, qty, name, type,partner_id, fposition_id, price_unit, currency_id,company_id)
        
        added_result = prev_result['value']
        
        added_result['sale_type'] = p.sale_type
        added_result['schedule_no'] = p.schedule_no
        added_result['item_sr_no'] = p.item_sr_no
        
        return {'value': added_result}