from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(GithubRawCommits)
admin.site.register(GithubRawReadmes)
admin.site.register(GithubRawRepos)
admin.site.register(GithubRawStars)
admin.site.register(GithubRawUsers)
admin.site.register(LinkedinRawProfiles)
admin.site.register(LinkedinRawSearchPeople)
admin.site.register(AllSourceUsersEnriched)
