import pytest
from datetime import datetime

# List to store test results
test_results = []

def generate_custom_report(report_path, results):
    report_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Custom Test Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            .status-passed { background-color: #d4edda; color: #155724; }
            .status-failed { background-color: #f8d7da; color: #721c24; }
        </style>
    </head>
    <body>
        <h1>Custom Test Report</h1>
        <table>
            <tr>
                <th>Test Case</th>
                <th>Status</th>
            </tr>
    """
    for result in results:
        status_class = "status-passed" if result['status'] == 'passed' else "status-failed"
        report_content += f"""
            <tr class="{status_class}">
                <td>{result['test_case']}</td>
                <td>{result['status']}</td>
            </tr>
        """
    report_content += """
        </table>
    </body>
    </html>
    """
    with open(report_path, "w") as report_file:
        report_file.write(report_content)

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        result = 'passed' if call.excinfo is None else 'failed'
        test_results.append({
            'test_case': item.name,
            'status': result
        })

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"E:/Newfolder/Yashas/Reports/custom_test_report_{timestamp}.html"
    generate_custom_report(report_path, test_results)
