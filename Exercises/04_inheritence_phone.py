import time


class Phone:
    """ Base class for all types of mobile phones """
    
    def __init__(self, name, screen_size, num_camera=2):
        self.name = name
        self.screen_size = screen_size
        self.num_of_camera = num_camera
        self.is_on = True  # power switch
        self.photos = []  # list of pictures taken
        self.calls = {}  # call log
    
    def switch_power(self):
#         self.is_on = False if self.is_on else True
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True
    
    def take_photo(self):
        """ Take a photo and append it to the photo album """
        self.photos.append([[1, 0], [0, 1]])
    
    def call(self, other):
        """ Call another Phone instance """
        if self.is_on and other.is_on:
            self.calls[other.name] = time.time()
            other.calls[self.name] = time.time()
        else:
            print(f"Phone {other.name} is off.")
            
        return other

class IPhone(Phone):
    """ A more expensive phone, that can call other iPhones using a special call method """
    
    def __init__(self, name, screen_size, num_camera, apple_id):
        super().__init__(name, screen_size, num_camera)
        self.apple_id = apple_id
        self.facetime_calls = {}  # FaceTime call log
    
    def call(self, other):
        """ Overrides the call method from the parent class """
        if self.is_on and other.is_on:
            try:
                self.facetime_calls[other.apple_id] = time.time()
            except AttributeError:
                self.calls[other.name] = time.time()
                other.calls[self.name] = time.time()
            else:
                other.facetime_calls[self.apple_id] = time.time()
        else:
            print(f"Phone {other.name} is off.")
        
        return other



regular = Phone(name='lg_v10', screen_size=6)
iphone = IPhone(name='iphone_8', screen_size=5.5, num_camera=3, apple_id='first_iphone_8')
iphone2 = IPhone(name='iphone_X', screen_size=6, num_camera=3, apple_id='second_iphone_X')

# Call from regular phone to iPhone
print(f"Before calling, the log for regular shows: {regular.calls}")
iphone = regular.call(iphone)
print(f"After the call, regular shows {regular.calls} and the iPhone shows {iphone.calls}")

# Two iPhones:
print(f"Before calling, the log for first iPhone shows: {iphone.facetime_calls}")
iphone2 = iphone.call(iphone2)
print(f"After the call, the first iPhone shows {iphone.facetime_calls} and the second shows {iphone2.facetime_calls}")