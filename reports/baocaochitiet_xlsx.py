from odoo import models

class BaoCaoChiTietXlsx(models.AbstractModel):
    _name = 'report.mockproject_ptd.baocaochitiet_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Báo cáo chi tiết')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': '#f2eee4', 'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})
        data_row_style = workbook.add_format({'bold': False, 'align': 'center', 'border': True})
        sheet.merge_range('A1:Y1', 'BÁO CÁO CHI TIẾT VỀ PHƯƠNG TIỆN ĐO LƯỜNG TRONG TOÀN TẬP ĐOÀN', title)
        date_format = workbook.add_format({'num_format': 'dd/mm/yy','bold': False, 'align': 'center', 'border': True})
        cell_format = workbook.add_format({'bold': True})


        # sheet.write(a,b,'c') : a_ row ; b_col, c_text(số thì k cần dấu ' ') (có thể tạo 1 cái)
        # sheet.merge_range(first_row, first_col, last_row, last_col, data [,merge_format]
        # sheet.set_column(first col, last_col, width [,cell_format]) (cột đầu tiên, cột cuối cùng, chiều rộng của các cột)


        sheet.merge_range('A3:A5', 'STT', merge_format)
        sheet.merge_range('B3:B5', 'Tên phương tiện đo', merge_format)
        sheet.merge_range('C3:C5', 'Mã hàng hóa', merge_format)
        sheet.merge_range('D3:D5', 'Part Number', merge_format)
        sheet.merge_range('E3:E5', 'Serial', merge_format)
        sheet.merge_range('F3:F5', 'Tình trạng', merge_format)
        sheet.merge_range('G3:G5', 'Thời gian đưa vào sử dụng', merge_format)

        sheet.merge_range('H3:J3', 'Thông tin quản lý', merge_format)
        sheet.merge_range('K3:N3', 'Phân cấp chất lượng', merge_format)
        sheet.merge_range('O3:U3', 'Công tác kiểm định / Hiệu chuẩn (KĐHC)', merge_format)

        sheet.write('V3', 'Công tác bảo trì, bảo dưỡng', merge_format)
        sheet.merge_range('W3:X3', 'Công tác bảo hành sửa chữa', merge_format)
        sheet.merge_range('Y3:Y5', 'Ghi chú', merge_format)

        # Trong thông tin quản lý
        sheet.merge_range('H4:H5', 'Mã nhân viên', merge_format)
        sheet.merge_range('I4:I5', 'Họ và tên', merge_format)
        sheet.merge_range('J4:J5', 'Đơn vị quản lý', merge_format)

        # Trong phân cấp chất lượng
        sheet.merge_range('K4:K5', 'Cấp 1', merge_format)
        sheet.merge_range('L4:L5', 'Cấp 2', merge_format)
        sheet.merge_range('M4:M5', 'Cấp 3', merge_format)
        sheet.merge_range('N4:N5', 'Cấp 4', merge_format)

        # Trong công tác kiểm định / hiệu chuẩn (KĐHC)
        sheet.merge_range('O4:O5', 'Chu kỳ kiểm định, hiệu chuẩn', merge_format)
        sheet.merge_range('P4:P5', 'Thời gian thực hiện KĐ/HC', merge_format)
        sheet.merge_range('Q4:Q5', 'Đối tác thực hiện KĐHC', merge_format)
        sheet.merge_range('R4:R5', 'Ghi rõ KĐ hay HC', merge_format)
        sheet.merge_range('S4:U4', 'Kết quả kiểm định / hiệu chuẩn', merge_format)
        sheet.write('S5', 'Đạt', merge_format)
        sheet.write('T5', 'Không đạt', merge_format)
        sheet.write('U5', 'Nguyên nhân không đạt', merge_format)

        # Trong công tác bảo trì bảo dưỡng
        sheet.merge_range('V4:V5', 'Thời gian thực hiện gần nhất', merge_format)
        #Trong công tác bảo hành sửa chữa
        sheet.merge_range('W4:W5', 'Thời gian hỏng gần nhất', merge_format)
        sheet.merge_range('X4:X5', 'Nguyên nhân hỏng', merge_format)

        sheet.set_column('A:A',5)
        sheet.set_column('B:B',20)
        sheet.set_column('C:C',12)
        sheet.set_column('D:D',11)
        sheet.set_column('E:E',10)
        sheet.set_column('F:F',13)
        sheet.set_column('G:G',25)

        sheet.set_column('H:J',50)
        sheet.set_column('H:H',15)
        sheet.set_column('I:I',15)
        sheet.set_column('J:J',20)

        sheet.set_column('K:N',20)
        sheet.set_column('K:K',5)
        sheet.set_column('L:L',5)
        sheet.set_column('M:M',5)
        sheet.set_column('N:N',5)

        sheet.set_column('O:O',27)
        sheet.set_column('P:P',25)
        sheet.set_column('Q:Q',21)
        sheet.set_column('R:R',17)
        #Công tác kiểm định / hiệu chuẩn (KĐHC)
        sheet.set_column('S:S',9)
        sheet.set_column('T:T',9)
        sheet.set_column('U:U',21)
        # Công tác bảo trì
        sheet.set_column('V:V',26)

        # Công tác sửa chữa
        sheet.set_column('W:W',22)
        sheet.set_column('X:X',18)
        # Ghi chú
        sheet.set_column('Y:Y',18)


        records = self.env['ptd.ptd'].search([])

        row = 5
        col = 0
        docs = []
        i = 1

        for record in records:
            quality_status = dict(record._fields['quality_status'].selection)
            # name = dict(record._fields['name'].selection)

            # Lấy ra ngày thực hiện gần nhất
            self.env.cr.execute(
                """SELECT max(implementation_date) FROM ptd_maintain_info 
                WHERE maintain_info_id = %s """ % (record.id))
            mainteinance_imple_date = self.env.cr.fetchone()
            print(mainteinance_imple_date)

            # Lấy ra kiểu KĐ hay HC
            self.env.cr.execute(
                """SELECT stand_link_type FROM ptd_check_or_correct
                    WHERE check_or_correct_id = %s """ % (record.id) +
                """and validity_date =
                (SELECT max(validity_date) FROM public.ptd_check_or_correct
                WHERE check_or_correct_id = %s """ % (record.id) + """)""")
            check_or_correct_stand_link = self.env.cr.fetchone()

            # Lấy ra name (fail hay pass) để in ra trường đạt hay không đạt
            self.env.cr.execute(
                """SELECT reason_not_pass FROM ptd_check_or_correct
                    WHERE check_or_correct_id = %s """ % (record.id) +
                """and validity_date =
                (SELECT max(validity_date) FROM public.ptd_check_or_correct
                WHERE check_or_correct_id = %s """ % (record.id) + """)""")
            check_or_correct_reason_not_pass = self.env.cr.fetchone()

            # Lấy ra nguyên nhân không đạt mới nhất
            self.env.cr.execute(
                """SELECT name FROM ptd_check_or_correct
                    WHERE check_or_correct_id = %s """ % (record.id) +
                """and validity_date =
                (SELECT max(validity_date) FROM public.ptd_check_or_correct
                WHERE check_or_correct_id = %s """ % (record.id) + """)""")
            check_or_correct_name = self.env.cr.fetchone()


            docs.append({
                'id' : i,
                'name': record.name,
                'commodity_code': record.commodity_code,
                # Part number
                'serial_number': record.serial_number,
                'quality_status': quality_status.get(record.quality_status),
                # Thời gian đưa vào sử dụng
                'manager_id1':record.manager_id.employee_code,
                'manager_id2':record.manager_id.name,
                'unit_manager_id':record.unit_manager_id.name,
                'quality_level':record.quality_level,
                'maintenance_cycle':record.maintenance_cycle,

                # 'reason_not_pass': record.check_or_correct_ids.reason_not_pass,
                'check_or_correct_stand_link':check_or_correct_stand_link[0],
                'mainteinance_imple_date': mainteinance_imple_date[0],
                'check_or_correct_name':check_or_correct_name[0],
                'check_or_correct_reason_not_pass':check_or_correct_reason_not_pass[0],
                'fail_time' : record.fail_time,
                'fail_reason' : record.fail_reason,
                'description' : record.description
            })
            i += 1
        for doc in docs:
            # Id
            sheet.write(row, col, doc['id'],data_row_style)
            # Tên thiết bị
            sheet.write(row, col + 1, doc['name'],data_row_style)
            # Mã hàng hóa
            sheet.write(row, col + 2, doc['commodity_code'],data_row_style)
            # Part number
            sheet.write(row,col+3, "",data_row_style)
            # Serial
            sheet.write(row, col + 4, doc['serial_number'],data_row_style)
            # Trạng thái
            sheet.write(row,col+5, doc['quality_status'], data_row_style)
            # Thời gian đưa vào sử dụng
            sheet.write(row,col+6, "",data_row_style)
            # Mã nhân viên
            sheet.write(row,col+7, doc['manager_id1'],data_row_style)
            # Họ và tên - Chưa làm
            sheet.write(row,col+8, doc['manager_id2'],data_row_style)
            # Đơn vị quản lý - Chưa làm
            sheet.write(row,col+9, doc['unit_manager_id'],data_row_style)
            # Cấp 1
            if doc['quality_level'] == '1':
                sheet.write(row, col+10, "x", data_row_style)
                sheet.write(row, col+11, "", data_row_style)
                sheet.write(row, col+12, "", data_row_style)
                sheet.write(row, col+13, "", data_row_style)

            if doc['quality_level'] == '2':
                sheet.write(row, col+10, "", data_row_style)
                sheet.write(row, col+11, "x", data_row_style)
                sheet.write(row, col+12, "", data_row_style)
                sheet.write(row, col+13, "", data_row_style)

            if doc['quality_level'] == '3':
                sheet.write(row, col+10, "", data_row_style)
                sheet.write(row, col+11, "", data_row_style)
                sheet.write(row, col+12, "x", data_row_style)
                sheet.write(row, col+13, "", data_row_style)

            if doc['quality_level'] == '4':
                sheet.write(row, col+10, "", data_row_style)
                sheet.write(row, col+11, "", data_row_style)
                sheet.write(row, col+12, "", data_row_style)
                sheet.write(row, col+13, "x", data_row_style)

            # Chu kì kiểm định hiệu chuẩn
            sheet.write(row,col+14, doc['maintenance_cycle'],data_row_style)
            # Thời gian thực hiện KĐHC gần nhất
            sheet.write(row,col+15, "",data_row_style)
            # Đối tác thực hiện KĐHC
            sheet.write(row,col+16, "",data_row_style)
            # Ghi rõ KĐ hay HC
            # sheet.write(row,col+17, "Đúng",data_row_style)
            if doc['check_or_correct_stand_link'] == "Kiểm định":
                sheet.write(row, col + 17, doc['check_or_correct_stand_link'], data_row_style)
            if doc['check_or_correct_stand_link'] == "Hiệu chỉnh":
                sheet.write(row, col + 17, doc['check_or_correct_stand_link'], data_row_style)
            if doc['check_or_correct_stand_link'] != "Kiểm định" and doc['check_or_correct_stand_link'] != "Hiệu chỉnh":
                sheet.write(row, col + 17, "Khác", data_row_style)

            #
            # sheet.write(row,col+18, "",data_row_style)
            # sheet.write(row,col+19, "",data_row_style)
            # sheet.write(row,col+20, "",data_row_style)


            # Đạt
            if doc['check_or_correct_name'] !='1' and doc['check_or_correct_name'] !='2':
                sheet.write(row, col + 18, "", data_row_style)
                sheet.write(row, col + 19, "", data_row_style)
                sheet.write(row, col + 20, "", data_row_style)
            if doc['check_or_correct_name'] =='1':
                sheet.write(row,col+18, "x",data_row_style)
                sheet.write(row,col+19, "",data_row_style)
                sheet.write(row,col+20, "",data_row_style)
            # # Không đạt
            # # Nguyên nhân không đạt
            if doc['check_or_correct_name'] =='2':
                sheet.write(row,col+18, "",data_row_style)
                sheet.write(row,col+19, "x",data_row_style)
                sheet.write(row,col+20, doc['check_or_correct_reason_not_pass'],data_row_style)
            # Thời gian thực hiện gần nhất
            if doc['mainteinance_imple_date'] == 'False':
                sheet.write(row,col+21,"",date_format)
            else:
                sheet.write(row,col+21, doc['mainteinance_imple_date'],date_format)

            # Viết hàm điều kiện
            sheet.write(row,col+22,doc["fail_time"],date_format)
            sheet.write(row,col+23,doc["fail_reason"],date_format)
            sheet.write(row,col+24, doc['description'],data_row_style)
            row += 1




