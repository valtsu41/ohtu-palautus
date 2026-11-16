*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Esa
    Set Password  12345678
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Es
    Set Password  12345678
    Click  button >> text=Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  Esa
    Set Password  1234567
    Click  button >> text=Register
    Register Should Fail With Message  Password too short

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  12345678
    Click  button >> text=Register
    Register Should Fail With Message  This username is already taken

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
