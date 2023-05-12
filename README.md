[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- PROJECT LOGO -->

<br />
<p align="center">
    <img src="Resources/logo.png" alt="Logo" height="100">

  <h3 align="center">Automation Exercise</h3>

  <p align="center">
    ...
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
Introduction

This is an selenium based framework that interacts with automationexercise Web App and can be used to automate given below

1. Navigate & Verify home page
2. Add Product to cart & verify
3. Verify Address, Place Order 
4. Pay & Confirm, Verify Order Placement

# Setup

1. Clone this repository
    ```
    git clone https://github.com/rfnshare/Automation-Exercise.git
    ```

2. If you clone this repository before then run this on the project's root directory
    ```
    git pull
    ```
3. Update your test data from Excel file. (Optional Feature)
    ```
    Test/TestData/test_data.xlsx
    ```
   
4. Go to the project's root directory and install requirements(Recommended create virtual env first).
    ```
    pip install -r requirements.txt
    ```

5. For Full Run this script from cmd line without report.
    ```
    python -m pytest -v -s
    ```

## Run Automated Tests

* To run all test cases in cmd line with html & allure report, run
```
python -m pytest -m <smoke/regression> --html=Reports/HTMLReports/index.html --self-contained-html -s --alluredir=./Reports/AllureReports/<smoke/regression>_report_allure
```
* Generate Allure HTML Report
```
allure serve ./Reports/AllureReports/<smoke/regression>_report_allure
```
* To run all test cases without cmd line, Go to project root directory & run `TestRunner.py` file by double click.
```
TestRunner.py
```
This will create an HTML, allure report. You can find report in Reports directory, report automatically will open in browser.
* You can configure Jenkins to parameterized run your test cases & generate html report, allure report, junit report. Also send mail to recipient.

## Sample Test Report

![Allure report screenshot](https://raw.githubusercontent.com/startrug/phptravels-selenium-py/screenshots/allure_report.png "Allure report screenshot")

Report is generated in a chosen browser.
### Usage


For more examples,  please refer to the [Documentation](https://example.com)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/rfnshare/Automation-Exercise/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

Abdullah Al Faroque - [@rfnshare](https://twitter.com/rfnshare) - aalfaroque@gmail.com

Project Link: [Automation Exercise](https://github.com/rfnshare/Automation-Exercise.git)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/contributors-0-yellow?style=for-the-badge
[contributors-url]: https://github.com/rfnshare/workspace-laznormal/graphs/contributors
[forks-shield]: https://img.shields.io/badge/froks-0-blue?style=for-the-badge
[forks-url]: https://github.com/rfnshare/workspace-laznormal/network/members
[stars-shield]: https://img.shields.io/badge/stars-0-red?style=for-the-badge
[stars-url]: https://github.com/rfnshare/workspace-laznormal/stargazers
[issues-shield]: https://img.shields.io/badge/issues-0-success?style=for-the-badge
[issues-url]: https://github.com/rfnshare/workspace-laznormal/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rfnshare
