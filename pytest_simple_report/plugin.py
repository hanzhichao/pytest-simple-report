from jinja2 import Template

DEFAULT_REPORT_TITLE = 'Pytest Simple Report'
DEFAULT_REPORT_TPL = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <style>
      table {border-spacing: 0;}
      th {background-color: #ccc}
      td {padding: 5px; border: 1px solid #ccc;}
    </style>
</head>
<body>
    <h2>{{title}}</h2>
    <table>
        <tr> <th>Test</th> <th>NodeId</th> <th>Status</th><th>Output</th> <th>Duration</th> </tr>
        {% for test in results %}
        <tr>
            <td>{{test.name}}</td>
            <td>{{test.id}}</td>
            <td>{{test.status}}</td>
            <td>{{test.output}}</td>
            <td>{{ test.duration }}s</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>'''


def pytest_addoption(parser):
    parser.addoption('--report', action='store', help='Report file')
    parser.addoption('--report-title', action='store', help='Report title')
    parser.addoption('--report-template', action='store', help='Report template file')
    parser.addini('report', help='Report file')
    parser.addini('report_title', help='Report file')
    parser.addini('report_template', help='Report template file')


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    report_file = config.getoption('--report') or config.getini('report')
    if report_file:
        title = config.getoption('--report-title') or config.getini('report_title') or DEFAULT_REPORT_TITLE
        template = config.getoption('--report-template') or config.getini('report_template') or DEFAULT_REPORT_TPL

        items = []
        for status in ['passed', 'failed', 'skipped', 'xfailed', 'xpassed']:
            if status in terminalreporter.stats:
                items.extend(terminalreporter.stats[status])

        # format
        results = []
        for item in items:
            test = {'id': item.nodeid, 'name': item.location[2], 'status': item.outcome,
                    'start_time': item.start, 'end_time': item.stop,
                    'output': item.sections[0][1].strip() if item.sections else '',
                    'duration': round(item.duration, 2)}
            results.append(test)

        html = Template(template).render(title=title, results=results)
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(html)
