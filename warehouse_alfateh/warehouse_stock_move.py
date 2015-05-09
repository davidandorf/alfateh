from openerp import models,  fields,  api
class warehouse_stock_move_custom(models.Model):
    _inherit = "stock.move"
    date = fields.Date(string="Date")
    date_expected = fields.Date(string="Expected Date")
    sale_type = fields.Selection([('1', 'Goods at standard rate'),  ('2', 'Third Schedule Goods'), ('3', 'Good at Reduced Rate'), ('4', 'Electricity Supply to Retailers'), ('5', 'Electricity to stell sector'), ('6', 'Gas to CNG stations'), ('7', 'Re-rollable scrap by ship-breakers'), ('8', 'SIM sale / IMEI activation')], "Sale Type")
    schedule_no = fields.Selection([('1', '(549(I)/2008'),  ('2', '811(I)/2009'), ('3', 'Zero Rated Elec.'), ('4', 'Zero Rated Gas'), ('5', '5th Schedule'), ('6', '1125(I)/2011'), ('7', '608(I)/2012'), ('8', '79(I)/2012'), ('9', '1st Schedule FED'), ('10', '1007(I)/2005'), ('11', '326(I)/2008'), ('12', '539(I)/2008'), ('13', '542(I)/2008'), ('14', '551(I)/2008'), ('15', '727(I)/2011'), ('16', '76(I)/2008'), ('17', '880(I)/2007'), ('18', '6th Schd Table I'), ('19', '6th Schd Table II'), ('20', 'DTRE'), ('21', 'FED 3rd Schd Table I'), ('22', 'FED 3rd Schd Table II'), ('23', 'Section 4(b)'), ('24', '802(I)/2009'), ('25', '678(I)/2004'), ('26', '760(I)/2012'), ('27', '213(I)/2013'), ('28', '499(I)/2013'), ('29', '501(I)/2013'), ('30', '670(I)/2013'), ('31', '657(I)/2013'), ('32', '898(I)/2013'), ('33', '896(I)/2013'), ('34', '460(I)/2013')], "SRO No. / Schedule No.")
    item_sr_no = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48'),('49','49'),('50','50'),('51','51'),('52','52'),('53','53'),('54','54'),('55','55'),('56','56'),('57','57'),('58','58'),('59','59'),('60','60'),('61','61'),('62','62'),('63','63'),('64','64'),('65','65'),('66','66'),('67','67'),('68','68'),('69','69'),('70','70'),('71','71'),('72','72'),('73','73'),('74','74'),('75','75'),('76','76'),('77','77'),('78','78'),('79','79'),('80','80'),('81','81'),('82','82'),('83','83'),('84','84'),('85','85'),('86','86'),('87','87'),('88','88'),('89','89'),('90','90'),('91','91'),('92','92'),('93','93'),('94','94'),('95','95'),('96','96'),('97','97'),('98','98'),('99','99'),('100','100'),('101','101'),('102','102'),('103','103'),('104','104'),('105','105'),('106','106'),('107','107'),('108','108'),('109','109'),('110','110'),('111','111'),('112','112'),('113','113'),('114','114'),('115','115'),('116','116'),('117','117'),('118','118'),('119','119'),('120','120'),('121','121'),('122','122'),('123','123'),('124','124'),('125','125'),('126','126'),('127','127'),('128','128'),('129','A'),('130','B'),('131','C'),('132','52A')], "Item Sr. No.")
    
    
    def onchange_product_id(self, cr, uid, ids, prod_id=False, loc_id=False, loc_dest_id=False, partner_id=False):
        if not prod_id:
            return {}
        user = self.pool.get('res.users').browse(cr, uid, uid)
        lang = user and user.lang or False
        if partner_id:
            addr_rec = self.pool.get('res.partner').browse(cr, uid, partner_id)
            if addr_rec:
                lang = addr_rec and addr_rec.lang or False
        ctx = {'lang': lang}

        product = self.pool.get('product.product').browse(cr, uid, [prod_id], context=ctx)[0]
        uos_id = product.uos_id and product.uos_id.id or False
        result = {
            'name': product.partner_ref,
            'product_uom': product.uom_id.id,
            'product_uos': uos_id,
            'product_uom_qty': 1.00,
            'product_uos_qty': self.pool.get('stock.move').onchange_quantity(cr, uid, ids, prod_id, 1.00, product.uom_id.id, uos_id)['value']['product_uos_qty'],
            'sale_type': product.sale_type,
            'schedule_no':product.schedule_no,
            'item_sr_no':product.item_sr_no
            
        }
        if loc_id:
            result['location_id'] = loc_id
        if loc_dest_id:
            result['location_dest_id'] = loc_dest_id
        return {'value': result}