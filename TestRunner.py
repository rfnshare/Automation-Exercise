import glob
import subprocess
import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Resources.ExcelUtils import read_configuration_data_from_excel
from Resources.GeneralUtils import read_date, read_time, get_html_reports

excel_path = Path(__file__).resolve().parent / "Test/TestData/test_data.xlsx"
configuration_data = read_configuration_data_from_excel(excel_path)

report_file_name_prefix = f"{read_date()}_{read_time()}"
test_type = configuration_data["test_type"]
run_command = (
    f"python -m pytest -m {test_type} -v -s -p no:warnings --html=Reports/HTMLReports/{test_type}_report_html/{test_type}_{report_file_name_prefix}_report.html "
    f"--self-contained-html "
    f"-v --junitxml=Reports/XMLReports/{test_type}_{report_file_name_prefix}_report.xml"
    f"-s --alluredir=Reports/AllureReports/{test_type}_report_allure/{report_file_name_prefix}"
)

subprocess.run(run_command, shell=True)

# send report if generated
# html_reports = get_html_reports(test_type)

# send report to receivers email
project_name = configuration_data["project_name"]
report_receiver_email = configuration_data["report_receiver"]
# send_report(report_receiver_email, html_reports, project_name)

# get html report name
report = os.path.abspath(
    glob.glob(f"Reports/HTMLReports/{test_type}_report_html/{test_type}_*.html")[-1]
)
print(report)

# html report open
html_open_report = f"start {report}"
# subprocess.run(html_open_report, shell=True)

# allure report serve
allure_serve_command = f"allure serve Reports/AllureReports/{test_type}_report_allure/{report_file_name_prefix}"
subprocess.run(allure_serve_command, shell=True)
