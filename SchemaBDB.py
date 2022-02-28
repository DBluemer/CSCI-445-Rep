#Incoming User Schema
import ipaddress
class UserSchema(BaseModel):
    incomingID: str = Field(..., max_length = 50, example="John Johnson")

class UserInfo(UserSchema):
    ipAddress: float = Field(...)
    macAddress: float = Field(...)


#Tracked User
class TrackedUser(BaseModel):
    trackedUserID: str = incomingID

class TrackedUserInfo(TrackedUser):
    tipAddress: float = ipAddress
    tmacAddress: float = macAddress

#Finding User
class SearchUser(BaseModel):
    trackedUserID: str = Field(..., max_length = 50, example="John Johnson")
    tipAddress: Optional[float]
    tmacAddress: Optional[float]

#Blocked User
class BlockedUser(BaseModel):
    blockedUserID: str = trackedUserID

class BlockedInfo(BlockedUser):
    bipAddress: float = tipAddress
    bmacAddress: float = tmacAddress

#Finding Blocked User
class SearchBlockedUser(BaseModel):
    blockedUserID: str = Field(..., max_length = 50, example="John Johnson")
    bipAddress: Optional[float]
    bmacAddress: Optional[float]
