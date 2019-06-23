from django import forms

class CredentialsForm(forms.Form):

    access_token = forms.CharField(required=True,
                                   label="access token")
    access_secret = forms.CharField(required=True,
                                    label="access secret")
    consumer_key = forms.CharField(required=True,
                                   label="consumer key")
    consumer_secret = forms.CharField(required=True,
                                      label="consumer secret")


    def clean(self):
        clean_data = self.cleaned_data
        print("cleaned_data==",clean_data)

class HashTagSearchForm(forms.Form):
    hash_tag = forms.CharField(required=True,
                               label="Hash Tag")

    def clean(self):
        cleaned_data = self.cleaned_data

class UserSearchForm(forms.Form):
    user_search = forms.CharField(required=True,
                                  label='User Search')

    def clean(self):
        cleaned_data = self.cleaned_data


class FollowersListForm(forms.Form):
    followers_list = forms.CharField(required=True,
                                     label='Get follower list')

    def clean(self):
        cleaned_data = self.cleaned_data