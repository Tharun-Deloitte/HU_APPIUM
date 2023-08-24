from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class Locators:

    # for signup page

    menuBtn_locator = ["Menu",(AppiumBy.ACCESSIBILITY_ID,'open menu')]



    UsernameInput=["Username",(AppiumBy.ACCESSIBILITY_ID,'Username input field')]
    PasswordInput=["Password",(AppiumBy.ACCESSIBILITY_ID,'Password input field')]
    LoginpageLoginBtn=["Log in",(AppiumBy.ACCESSIBILITY_ID,'Login button')]
    detailsNotMatch=["Login Error msg",(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView')]

    productNames=['Product names',(AppiumBy.ACCESSIBILITY_ID,'store item text')]
    ProductPrices=['Product prices',(AppiumBy.ACCESSIBILITY_ID,'store item price')]
    ProductName=['Product name',(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="container header"]/android.widget.TextView')]
    ProductPrice=['Product price',(AppiumBy.ACCESSIBILITY_ID,'product price')]
    ProductQuantity=['Product quantity',(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="counter amount"]/android.widget.TextView')]
    srot=['Sort',(AppiumBy.ACCESSIBILITY_ID,'sort button')]
    NameAscen=['Name/Asce',(AppiumBy.ACCESSIBILITY_ID,'nameAsc')]
    NameDescen=['Name/Descen',(AppiumBy.ACCESSIBILITY_ID,'nameDesc')]
    PriceAscen=['PriceAsce',(AppiumBy.ACCESSIBILITY_ID,'priceAsc')]
    PriceDescen=['PriseCescen',(AppiumBy.ACCESSIBILITY_ID,'priceDesc')]
    Addtocart=['Add to cart',(AppiumBy.ACCESSIBILITY_ID,'Add To Cart button')]
    GoToCart=['Cart',(AppiumBy.ACCESSIBILITY_ID,'cart badge')]
    MyDemoApp=["My Demo App text",(AppiumBy.ACCESSIBILITY_ID,'longpress reset app')]




    cartcount=['Cart count',(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="cart badge"]/android.widget.TextView')]
    removeitem=['Remove item',(AppiumBy.ACCESSIBILITY_ID,'remove item')]
    ProceedtoCheckOut=['Proceed to checkout',(AppiumBy.ACCESSIBILITY_ID,'Proceed To Checkout button')]
    cartpageProductNames=['Product names',(AppiumBy.ACCESSIBILITY_ID,'product label')]
    cartpageProductQuantity=['Product quantity',(AppiumBy.XPATH,'(//android.view.ViewGroup[@content-desc="counter amount"])/android.widget.TextView')]

    FullName=['Full name',(AppiumBy.ACCESSIBILITY_ID,'Full Name* input field')]
    Address1=['Address1',(AppiumBy.ACCESSIBILITY_ID,'Address Line 1* input field')]
    City=['City',(AppiumBy.ACCESSIBILITY_ID,'City* input field')]
    State=['State',(AppiumBy.ACCESSIBILITY_ID,'State/Region input field')]
    PinCode=['Pincode',(AppiumBy.ACCESSIBILITY_ID,'Zip Code* input field')]
    Country=['Country',(AppiumBy.ACCESSIBILITY_ID,'Country* input field')]
    ToPayment=['Payment page',(AppiumBy.ACCESSIBILITY_ID,'To Payment button')]

    PaymentPageFullName=['Full name',(AppiumBy.ACCESSIBILITY_ID,'Full Name* input field')]
    Cardnumber=['Card number',(AppiumBy.ACCESSIBILITY_ID,'Card Number* input field')]
    Cvv=['CVV',(AppiumBy.ACCESSIBILITY_ID,'Security Code* input field')]
    Expirydate=['Expiry date',(AppiumBy.ACCESSIBILITY_ID,'Expiration Date* input field')]
    ReviewOrder=['Review order',(AppiumBy.ACCESSIBILITY_ID,'Review Order button')]
    CardnumErrorMsg=['Card num error msg',(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Card Number*-error-message"]/android.widget.TextView')]
    ExpirationdateErrorMsg=['Expiry date error msg',(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Expiration Date*-error-message"]/android.widget.TextView')]
    CvvErrorMsg=['CVV error msg',(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Security Code*-error-message"]/android.widget.TextView')]


    ReviewPageProductPrice=['Product price',(AppiumBy.ACCESSIBILITY_ID,'product price')]
    ReviewPageProductName=['Product Name',(AppiumBy.ACCESSIBILITY_ID,'product label')]
    PlaceOrder=['Place order',(AppiumBy.ACCESSIBILITY_ID,'Place Order button')]

    ContinueShopping=['Continue Shopping',(AppiumBy.ACCESSIBILITY_ID,'Continue Shopping button')]
    OrderDispatched=['Order Dispatched',(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="checkout complete screen"]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[4]')]

    logout=['Log out',(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="menu item log out"]')]
    popuplogout=['log out confirmation',(AppiumBy.ID,'android:id/button1')]
    succseefullogoutmsg=['Log out success msg', (AppiumBy.ID, 'android:id/alertTitle')]
    SuccessOk=['Log out success Pop up',(AppiumBy.ID,'android:id/button1')]


    options_Catlog=['Catlog',(AppiumBy.ACCESSIBILITY_ID,'menu item catalog')]
    options_WebView=['Webiew',(AppiumBy.ACCESSIBILITY_ID,'menu item webview')]
    options_QRCode=['QR Code',(AppiumBy.ACCESSIBILITY_ID,'menu item qr code scanner')]
    options_GeoLocation=['Geo Location',(AppiumBy.ACCESSIBILITY_ID,'menu item geo location')]
    options_Draw=['Draw',(AppiumBy.ACCESSIBILITY_ID,'menu item drawing')]
    options_About=['About',(AppiumBy.ACCESSIBILITY_ID,'menu item about')]
    options_Reset=['Reset',(AppiumBy.ACCESSIBILITY_ID,'menu item reset app')]
    options_FingerPrint=['Finger Print',(AppiumBy.ACCESSIBILITY_ID,'menu item biometrics')]
    options_LogIN=['Log in',(AppiumBy.ACCESSIBILITY_ID,'menu item log in')]
    options_LogOut=['Log out',(AppiumBy.ACCESSIBILITY_ID,'menu item log out')]
    options_APICalls=['API Calls',(AppiumBy.ACCESSIBILITY_ID,'menu item api calls')]
    options_BotVideo=['Sauce Bot video',(AppiumBy.ACCESSIBILITY_ID,'menu item sauce bot video')]



