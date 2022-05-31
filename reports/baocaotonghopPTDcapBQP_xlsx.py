from odoo import models


class BaoCaoChiTietXlsx(models.AbstractModel):
    _name = 'report.mockproject_ptd.baocaotonghopptdcapbqp_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Báo cáo tổng hợp PTĐ cấp BQP')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': '#f2eee4', 'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True,})
        data_row_style = workbook.add_format({'bold': False, 'align': 'center', 'border': True})
        text_format = workbook.add_format({'text_wrap': True,'align':'center','border':True})
        sheet.merge_range('A1:M1', 'BÁO CÁO TỔNG HỢP PTĐ CẤP BQP', title)
        date_format = workbook.add_format({'num_format': 'dd/mm/yy'})
        cell_format = workbook.add_format({'bold': True})

        # sheet.write(a,b,'c') : a_ row ; b_col, c_text(số thì k cần dấu ' ') (có thể tạo 1 cái)
        # sheet.merge_range(first_row, first_col, last_row, last_col, data [,merge_format]
        # sheet.set_column(first col, last_col, width [,cell_format]) (cột đầu tiên, cột cuối cùng, chiều rộng của các cột)

        sheet.merge_range('A3:A4', 'STT', merge_format)
        sheet.merge_range('B3:B4', 'Số quản lý', merge_format)
        sheet.merge_range('C3:C4', 'Tên trang bị ĐL-TN', merge_format)
        sheet.merge_range('D3:D4', 'Ký hiệu', merge_format)
        sheet.merge_range('E3:E4', 'Số hiệu', merge_format)
        sheet.merge_range('F3:F4', 'Nước (hãng) SX', merge_format)
        sheet.merge_range('G3:G4', 'Năm sản xuất', merge_format)
        sheet.merge_range('H3:H4', 'Đặc tính đo lường chủ yếu', merge_format)
        sheet.merge_range('I3:I4', 'Cấp CL', merge_format)
        sheet.merge_range('J3:J4', 'Đơn vị quản lý', merge_format)
        sheet.merge_range('L3:L4', 'Chu kỳ KĐ/HC', merge_format)
        sheet.merge_range('K3:K4', 'Nơi KĐ/HC', merge_format)
        sheet.merge_range('M3:M4', 'Ghi chú', merge_format)

        sheet.set_column('A:A', 5)
        sheet.set_column('B:B', 13)
        sheet.set_column('C:C', 20)
        sheet.set_column('D:D', 10)
        sheet.set_column('E:E', 10)
        sheet.set_column('F:F', 14)
        sheet.set_column('G:G', 14)
        sheet.set_column('H:H', 27)
        sheet.set_column('I:I', 8)
        sheet.set_column('J:J', 15)
        sheet.set_column('K:K', 16)
        sheet.set_column('L:L', 12)
        sheet.set_column('M:M', 15)

        row = 4
        col = 0

        records = self.env['ptd.ptd'].search([])
        print(records)
        docs = []
        i = 1

        for record in records:
            self.env.cr.execute(
                """SELECT organisation_id FROM ptd_check_or_correct
                    WHERE check_or_correct_id = %s """ % (record.id) +
                """and validity_date =
                (SELECT max(validity_date) FROM public.ptd_check_or_correct
                WHERE check_or_correct_id = %s """ % (record.id) + """)""")
            check_or_correct_name = self.env.cr.fetchone()
            # self.env.cr.execute(
            #     """SELECT max(validity_date) FROM ptd_check_or_correct WHERE check_or_correct_id = %s """ %
            #     (record.id))
            # print(check_or_correct_name)

            # doc2s = []
            # doc2s.append({
            #     'check_or_correct_name' :check_or_correct_name.name[-1]
            # })
            docs.append({
                'id': i,
                'model': record.model,
                # Số quản lý
                'type_equip_id':record.type_equip_id.name,
                # Tên trang bị ĐL-TN
                'serial_number': record.serial_number,
                'country_id' : record.country_id.name,
                'year_manufacture':record.year_manufacture,
            # Đặc tính đo lường kĩ thuật
                'technical_characteristics_ids1':record.technical_characteristics_ids.parameters,
                'technical_characteristics_ids2':record.technical_characteristics_ids.val_maintain,
                'technical_characteristics_ids3':record.technical_characteristics_ids.exact_level,
                'quality_level' : record.quality_level,
            # Đơn vị quản lý
                'unit_manager_id' :record.unit_manager_id.name,
            # Nơi KĐ/HC
                'check_or_correct_name': check_or_correct_name[0],
                'maintenance_cycle':record.maintenance_cycle,
                'description' :record.description,
                'level_BQP' :record.level_BQP,
            })
            i += 1
        print(docs)
        # print(doc2s)
        for doc in docs:
            sheet.write(row, col, doc['id'], data_row_style)
            if doc['level_BQP'] == True:
                sheet.write(row, col+1,"",data_row_style)
                sheet.write(row, col+2,doc['type_equip_id'],data_row_style)
                sheet.write(row, col+3, doc['model'],data_row_style)
                sheet.write(row, col+4, doc['serial_number'],data_row_style)
                sheet.write(row, col+5,doc['country_id'],data_row_style)
                sheet.write(row, col+6,doc["year_manufacture"],data_row_style)

                if doc['technical_characteristics_ids1'] !='':
                    sheet.write(row, col+7,doc['technical_characteristics_ids1'],text_format)
                    # sheet.write(row, col+7,doc['technical_characteristics_ids2'],text_format)
                    # sheet.write(row, col+7,doc['technical_characteristics_ids3'],text_format)

                if doc['technical_characteristics_ids1'] =='':
                    sheet.write(row, col+7,"",data_row_style)

                sheet.write(row, col+8,doc["quality_level"],data_row_style)
                sheet.write(row, col+9,doc["unit_manager_id"],data_row_style)

                if doc["check_or_correct_name"] != '':
                    sheet.write(row, col+10,doc["check_or_correct_name"],data_row_style)

                sheet.write(row, col+11,doc['maintenance_cycle'],data_row_style)
                sheet.write(row, col+12,doc['description'],data_row_style)
            else:
                # sheet.write(row, col, "", data_row_style)
                sheet.write(row, col + 1, "", data_row_style)
                sheet.write(row, col + 2, "", data_row_style)
                sheet.write(row, col + 3, "", data_row_style)
                sheet.write(row, col + 4, "", data_row_style)
                sheet.write(row, col + 5, "", data_row_style)
                sheet.write(row, col + 6, "", data_row_style)
                sheet.write(row, col + 7, "", data_row_style)
                sheet.write(row, col + 8, "", data_row_style)
                sheet.write(row, col + 9, "", data_row_style)
                sheet.write(row, col + 10, "", data_row_style)
                sheet.write(row, col + 11, "", data_row_style)
                sheet.write(row, col + 12, "", data_row_style)
            row += 1

        # for doc2 in doc2s:
        #     if doc2["check_or_correct_name"] != '':
        #         sheet.write(row, col + 10, doc2["check_or_correct_name"], data_row_style)




