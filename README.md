# wetravel
It is hard to login user with auto-tests because of captcha. It is possible to use Chrome profile for example but it easier to turn off captcha for test.
To run test:
1. Make sure that you have python3 installed.
2. Clone repo
3. Open test folder as project in your IDE (Pycharm community edition: https://www.jetbrains.com/ru-ru/pycharm/download/)
4. Use  ```pip3 install -r requirements.txt``` in test folder
5. Run test with ```py.test --alluredir=%name of test result folder%  test*```
6. Run report ```allure serve %name of test result folder%```. You can see the link in terminal if browser doesn't open.
