import TestScript1
classNameObject = TestScript1.classScript1()

def sample():
    print("-------------------------------------------------------------")
    print("Log: Sign In Flow 1")
    classNameObject.sign_in()
    classNameObject.edit_profile()
    classNameObject.edit_security()
    classNameObject.sign_in_new_password()
    classNameObject.edit_security_revert_password()
