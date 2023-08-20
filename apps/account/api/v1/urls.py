from django.urls import path, include

from apps.account.api.v1.views import RegisterAPIView, LoginAPIView, VerifyPhoneNumberAPIView, \
    ReVerifyPhoneNumberAPIView, ChangePasswordCompletedView, LogoutView, UserProfileListView, \
    PersonalUserProfileDetailView, me, AboutMeListView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('verify/', VerifyPhoneNumberAPIView.as_view()),
    path('re-verify-code/', ReVerifyPhoneNumberAPIView.as_view()),
    path('change-pasword/<str:phone_number>/', ChangePasswordCompletedView.as_view()),

    path('users/', UserProfileListView.as_view()),
    path('<str:phone_number>/', PersonalUserProfileDetailView.as_view()),
    # path('me/', me),
    path('me/<str:phone_number>/', AboutMeListView.as_view()),
]
