from odoo import models

class PtdMeasuringDeviceXlsxReport(models.AbstractModel):
    _name = 'report.vss_ptd.measuring_device_xlsx_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Viettel')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': '#f2eee4', 'border': True})
        header_row_style = workbook.add_format({'bold': True, 'align': 'center', 'border': True})
        #
        sheet.merge_range('A1:Z1', 'BÁO CÁO CHI TIẾT VỀ PHƯƠNG TIỆN ĐO LƯỜNG TRONG TOÀN TẬP ĐOÀN', title)
        format_date = workbook.add_format({'num_format': 'dd/mm/yy'})
        #
        row = 3
        col = 0
        #
        # # Header row
        sheet.set_column(0, 28, 20)
        sheet.merge_range('A4:A6', 'STT', header_row_style)
        sheet.merge_range('B4:B6', 'Tên phương tiện đo', header_row_style)
        sheet.merge_range('C4:C6', 'Mã hàng hóa', header_row_style)
        sheet.merge_range('D4:D6', 'Serial', header_row_style)
        sheet.merge_range('E4:E6', 'Tình trạng', header_row_style)
        sheet.merge_range('F4:F6', 'Thời gian đưa vào sử dụng', header_row_style)

        # sheet.merge_range(row, col + 5, row + 1, col +7, 'EXCEL REPORT', header_row_style)
        sheet.merge_range('F4:H4', 'Thông tin quản lý', header_row_style)
        sheet.merge_range('I4:L4', 'Phân cấp chất lượng', header_row_style)
        sheet.merge_range('M4:S4', 'Công tác kiểm định/Hiệu chuẩn (KĐHC)', header_row_style)
        sheet.merge_range('U4:V4', 'Công tác bảo hành sửa chữa', header_row_style)
        # sheet.write(row, col+5, 'Thông tin quản lí', header_row_style)
        # sheet.write(row, col + 6, 'Phân cấp chất lượng', header_row_style)
        # sheet.write(row, col + 7, 'Công tác kiểm định/Hiệu chuẩn (KĐHC)', header_row_style)
        # sheet.write(row, col + 8, 'Công tác bảo trì, bảo dưỡng', header_row_style)
        # sheet.write(row, col + 9, 'Công tác bảo hành sửa chữa', header_row_style)
        sheet.write(row, col + 19, 'Công tác bảo trì, bảo dưỡng', header_row_style)
        sheet.write(row, col + 22, 'Ghi chú', header_row_style)

        # Người quản lý trực tiếp
        sheet.merge_range('F5:F6', 'Người quản lý trực tiếp', header_row_style)
        sheet.merge_range('G5:G6', 'Đơn vị quản lý trực tiếp', header_row_style)
        sheet.merge_range('H5:H6', 'Đơn vị quản lí cấp 1', header_row_style)
        # Phân cấp chất lượng
        # sheet.write(row + 1, col + 8, 'Cấp 1', header_row_style)
        # sheet.write(row + 1, col + 9, 'Cấp 2', header_row_style)
        # sheet.write(row + 1, col + 10, 'Cấp 3', header_row_style)
        # sheet.write(row + 1, col + 11, 'Cấp 4', header_row_style)
        sheet.merge_range('I5:I6', 'Cấp 1', header_row_style)
        sheet.merge_range('J5:J6', 'Cấp 2', header_row_style)
        sheet.merge_range('K5:K6', 'Cấp 3', header_row_style)
        sheet.merge_range('L5:L6', 'Cấp 4', header_row_style)

        # Công tác kiểm định hiệu chuẩn
        sheet.merge_range('M5:M6', 'Chu kì kiểm định hiệu chuẩn', header_row_style)
        sheet.merge_range('N5:N6', 'Thời gian thực hiện KĐHC gần nhất', header_row_style)
        sheet.merge_range('O5:O6', 'Đối tác thực hiện KĐHC', header_row_style)
        sheet.merge_range('P5:P6', 'Ghi rõ KĐ hay HC', header_row_style)

        sheet.merge_range('Q5:S5', 'Kết quả kiểm định/ hiệu chuẩn', header_row_style)
        # Công tác bảo trì
        sheet.merge_range('Q6:S5', 'Kết quả kiểm định/ hiệu chuẩn', header_row_style)

        sheet.write(row + 2, col + 16, 'Đạt', header_row_style)
        sheet.write(row + 2, col + 17, 'Không đạt', header_row_style)
        sheet.write(row + 2, col + 18, 'Nguyên nhân không đạt', header_row_style)

        sheet.merge_range('T5:T6', 'Thời gian thực hiện gần nhất', header_row_style)
        sheet.merge_range('U5:U6', 'Thời gian hỏng gần nhất', header_row_style)
        sheet.merge_range('V5:V6', 'Nguyên nhân hỏng', header_row_style)
        sheet.merge_range('W4:W6', 'Ghi chú', header_row_style)

        unit_manager_id = data['form']['unit_manager_id']
        records = self.env['ptd.measuring.device'].search([('unit_manager_id', '=', unit_manager_id)])

        docs = []
        i = 1
        for record in records:
            canonical_link_info_ids = self.env['ptd.canonical.link.info'].search([('active', '=', True),
                                                                                  ('canonical_link_info_id', '=',
                                                                                   record.id)])
            quality_status = dict(record._fields['quality_status'].selection)
            stand_link_type = dict(record._fields['stand_link_type'].selection)
            result = dict(canonical_link_info_ids._fields['result'].selection)
            docs.append({
                'id': i,
                'name': record.name,
                'asset_code': record.asset_code,
                'serial_number': record.serial_number,
                'quality_status': quality_status.get(record.quality_status),
                'year_use': record.year_use,
                'manager_id': record.manager_id.name,
                'unit_manager_id': record.unit_manager_id.name,
                'unit_manager_lever1_id': record.unit_manager_lever1_id.name,
                'user_id': record.user_id.name,
                'quality_level': record.quality_level,
                'stand_link_cycle': record.stand_link_cycle,
                'canonical_imple_date': canonical_link_info_ids.imple_date,
                'origanisation': canonical_link_info_ids.organisation,
                'stand_link_type': stand_link_type.get(record.stand_link_type),
                'result': result.get(canonical_link_info_ids.result),
                'canonical_fail_reason': canonical_link_info_ids.fail_reason,
                'fail_date': record.fail_date,
                'fail_reason': record.fail_reason,
                'description': record.description
            })
            i += 1
        print(docs)
        for doc in docs:
            for x in doc:
                if doc[x] == False:
                    doc[x] = ''
        row += 8
        for doc in docs:
            sheet.write(row, col, doc['id'])
            sheet.write(row, col + 1, doc['name'])
            sheet.write(row, col + 2, doc['asset_code'])
            sheet.write(row, col + 3, doc['serial_number'])
            sheet.write(row, col + 4, doc['quality_status'])
            sheet.write(row, col + 5, doc['year_use'], format_date)
            sheet.write(row, col + 6, doc['manager_id'])
            sheet.write(row, col + 7, doc['unit_manager_id'])
            sheet.write(row, col + 8, doc['unit_manager_lever1_id'])
            sheet.write(row, col + 9, doc['quality_level'])

            sheet.write(row, col + 13, doc['stand_link_cycle'])
            sheet.write(row, col + 14, doc['canonical_imple_date'])
            sheet.write(row, col + 15, doc['origanisation'])
            sheet.write(row, col + 16, doc['stand_link_type'])

            sheet.write(row, col + 17, doc['result'])
            sheet.write(row, col + 19, doc['canonical_fail_reason'])

            sheet.write(row, col + 20, doc['mainteinance_imple_date'])
            sheet.write(row, col + 21, doc['fail_date'])
            sheet.write(row, col + 22, doc['fail_reason'])
            sheet.write(row, col + 23, doc['description'])
            row += 1


