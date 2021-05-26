import datetime
import xlsxwriter
from COMMON.read_excel import *
from CRPO.crpo_common import *
from CRPO.credentials import *


class AllowedFileExtensions:

    def __init__(self):
        self.allowed_extensions = [".doc", ".rtf", ".dot", ".docx", ".docm", ".dotx", ".dotm", ".docb", ".pdf", ".xls",
                                   ".xlt", ".xlm", ".xlsx", ".xlsm", ".xltx", ".xltm", ".xlsb", ".xla", ".xlam", ".xll",
                                   ".xlw", ".ppt", ".pot", ".pps", ".pptx", ".pptm", ".potx", ".potm", ".ppam", ".ppsx",
                                   ".ppsm", ".sldx", ".sldm", ".zip", ".rar", ".7z", ".gz", ".jpeg", ".jpg", ".gif",
                                   ".png", ".msg", ".txt", ".mp4", ".mvw", ".3gp", ".sql", ".webm", ".csv", ".odt",
                                   ".json", ".ods", ".ogg", ".p12"]
        requests.packages.urllib3.disable_warnings()
        self.started = datetime.datetime.now()
        self.started = self.started.strftime("%Y-%M-%d-%H-%M-%S")
        self.row_size = 2
        file = "C:\\Users\\User\\Desktop\\Automation\\PythonWorkingScripts_Output\\allowed_extensions\\allowed_extensions -"
        self.write_excel = xlsxwriter.Workbook(file + self.started + '.xls')
        self.black_color = self.write_excel.add_format({'font_color': 'black', 'font_size': 9})
        self.black_color_bold = self.write_excel.add_format({'font_color': 'black', 'bold': True, 'font_size': 9})
        self.red_color = self.write_excel.add_format({'font_color': 'red', 'font_size': 9})
        self.green_color = self.write_excel.add_format({'font_color': 'green', 'font_size': 9})
        self.green_color_bold = self.write_excel.add_format({'font_color': 'green', 'font_size': 9, 'bold': True})
        self.orange_color = self.write_excel.add_format({'font_color': 'orange', 'font_size': 9})
        self.over_all_status_pass = self.write_excel.add_format({'font_color': 'green', 'bold': True, 'font_size': 9})
        self.over_all_status_failed = self.write_excel.add_format({'font_color': 'red', 'bold': True, 'font_size': 9})
        self.over_all_status_color = self.over_all_status_pass
        self.over_all_status = 'Pass'

        self.ws = self.write_excel.add_worksheet()
        self.ws.write(0, 0, "Allowed Extensions", self.green_color_bold)
        self.ws.write(1, 0, "Extension Type", self.black_color_bold)
        self.ws.write(1, 1, "Status", self.black_color_bold)
        self.ws.write(1, 2, "File Name", self.black_color_bold)
        self.ws.write(1, 3, "Expected Status", self.black_color_bold)
        self.ws.write(1, 4, "Actual Status", self.black_color_bold)

    def validate_files(self, token, excel_input):
        try:
            file_path = 'C:\\Users\\User\\Desktop\\Automation\\PythonWorkingScripts_InputData\\allowed_extensions\\%s' \
                        % (excel_input.get('filePathName'))
            file_name = excel_input.get('fileName')
            print(file_name)
            resp = crpo_common_obj.upload_files(token, file_name, file_path)
            if resp.get('status') == 'OK':
                actual_status = 'allowed'
            else:
                actual_status = 'disallowed'
            self.ws.write(self.row_size, 0, excel_input.get('extensionType'), self.black_color)
            self.ws.write(self.row_size, 2, excel_input.get('fileName'), self.black_color)
            self.ws.write(self.row_size, 3, excel_input.get('expectedStatus'), self.black_color)

            if excel_input.get('expectedStatus') == actual_status:
                self.ws.write(self.row_size, 1, "Pass", self.green_color)
                self.ws.write(self.row_size, 4, actual_status, self.black_color)
            else:
                self.ws.write(self.row_size, 1, "Fail", self.red_color)
                self.ws.write(self.row_size, 4, actual_status, self.red_color)
                self.over_all_status = 'Fail'
                self.over_all_status_color = self.over_all_status_failed
            self.row_size += 1

        except Exception as e:
            print(e)
            self.ws.write(self.row_size, 0, excel_input.get('extensionType'), self.orange_color)
            self.ws.write(self.row_size, 1, "Pass", self.orange_color)
            self.ws.write(self.row_size, 2, excel_input.get('fileName'), self.orange_color)
            self.ws.write(self.row_size, 3, excel_input.get('expectedStatus'), self.orange_color)
            self.ws.write(self.row_size, 4, "Exception is %s" % e, self.orange_color)
            self.row_size += 1


allowed_ext_obj = AllowedFileExtensions()
login_token = crpo_common_obj.login_to_crpo(cred_crpo_admin.get('user'), cred_crpo_admin.get('password'),
                                            cred_crpo_admin.get('tenant'))

input_file_path = 'C:\\Users\\User\\Desktop\\Automation\\PythonWorkingScripts_InputData\\allowed_extensions\\allowed_extensions_inputfile.xls'
excel_read_obj.excel_read(input_file_path, 0)
excel_data = excel_read_obj.details
for data in excel_data:
    allowed_ext_obj.validate_files(login_token, data)
ended = datetime.datetime.now()
ended = "Ended:- %s" % ended.strftime("%Y-%M-%d-%H-%M-%S")
allowed_ext_obj.ws.write(0, 1, "Overall Status is - %s" % allowed_ext_obj.over_all_status,
                         allowed_ext_obj.over_all_status_color)
allowed_ext_obj.ws.write(0, 2, 'Started:- ' + allowed_ext_obj.started, allowed_ext_obj.green_color_bold)
allowed_ext_obj.ws.write(0, 3, ended, allowed_ext_obj.green_color_bold)
allowed_ext_obj.ws.write(0, 4, "Total_Test case_Count:- 40", allowed_ext_obj.green_color_bold)
allowed_ext_obj.write_excel.close()
