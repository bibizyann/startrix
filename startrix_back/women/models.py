# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GithubRawCommits(models.Model):
    sha = models.TextField(blank=True, null=True)
    commited_at = models.DateTimeField(blank=True, null=True)
    author_name = models.TextField(blank=True, null=True)
    best_email = models.TextField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    author_login = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'github_raw_commits'


class GithubRawReadmes(models.Model):
    repo_id = models.BigIntegerField(blank=True, null=True)
    readme = models.TextField(blank=True, null=True)
    readme_tokens = models.FloatField(blank=True, null=True)
    parsed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'github_raw_readmes'


class GithubRawRepos(models.Model):
    archived = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    default_branch = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fork = models.BooleanField(blank=True, null=True)
    forks_count = models.BigIntegerField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    has_issues = models.BooleanField(blank=True, null=True)
    has_projects = models.BooleanField(blank=True, null=True)
    has_wiki = models.BooleanField(blank=True, null=True)
    has_downloads = models.BooleanField(blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    license_key = models.TextField(blank=True, null=True)
    license_name = models.TextField(blank=True, null=True)
    license_spdx_id = models.TextField(blank=True, null=True)
    mirror_url = models.TextField(blank=True, null=True)
    open_issues_count = models.BigIntegerField(blank=True, null=True)
    owner_node_id = models.TextField(blank=True, null=True)
    owner_id = models.BigIntegerField(blank=True, null=True)
    owner_login = models.TextField(blank=True, null=True)
    owner_site_admin = models.BooleanField(blank=True, null=True)
    owner_type = models.TextField(blank=True, null=True)
    pushed_at = models.DateTimeField(blank=True, null=True)
    repo_id = models.BigIntegerField(blank=True, null=True)
    node_id = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    stargazers_count = models.BigIntegerField(blank=True, null=True)
    commits_count = models.FloatField(blank=True, null=True)
    topics = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    watchers_count = models.BigIntegerField(blank=True, null=True)
    latest_commit_date = models.DateTimeField(blank=True, null=True)
    has_pages = models.BooleanField(blank=True, null=True)
    parsed_at = models.DateTimeField(blank=True, null=True)
    is_readme = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'github_raw_repos'


class GithubRawStars(models.Model):
    repo_id = models.BigIntegerField(blank=True, null=True)
    starred_at = models.DateTimeField(blank=True, null=True)
    parsed_at = models.DateTimeField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_node_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'github_raw_stars'


class GithubRawUsers(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    node_id = models.TextField(blank=True, null=True)
    login = models.TextField(blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    site_admin = models.BooleanField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    blog = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    hireable = models.BooleanField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    twitter_username = models.TextField(blank=True, null=True)
    public_repos = models.BigIntegerField(blank=True, null=True)
    public_gists = models.BigIntegerField(blank=True, null=True)
    followers = models.BigIntegerField(blank=True, null=True)
    following = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    socials = models.TextField(blank=True, null=True)
    parsed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'github_raw_users'


class LinkedinRawProfiles(models.Model):
    urn_id = models.TextField(blank=True, null=True)
    profile_link = models.TextField(blank=True, null=True)
    firstname = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase.
    locationname = models.TextField(db_column='locationName', blank=True, null=True)  # Field name made lowercase.
    geolocationname = models.TextField(db_column='geoLocationName', blank=True, null=True)  # Field name made lowercase.
    headline = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    student = models.BooleanField(blank=True, null=True)
    industryname = models.TextField(db_column='industryName', blank=True, null=True)  # Field name made lowercase.
    experiences = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    parsed_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkedin_raw_profiles'


class LinkedinRawSearchPeople(models.Model):
    urn_id = models.TextField(blank=True, null=True)
    jobtitle = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    parsed_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkedin_raw_search_people'


class AllSourceUsersEnriched(models.Model):
    utc_update_time = models.CharField(blank=True, null=True)
    user_id = models.CharField(primary_key=True)
    source_user_id = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    jobtitle = models.CharField(blank=True, null=True)
    programming_languages = ArrayField(models.CharField(blank=True, null=True))  # This field type is a guess.
    country = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    source = models.CharField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    contacts = ArrayField(models.CharField(blank=True, null=True, default=0))  # This field type is a guess.
    image_url = models.CharField(blank=True, null=True)
    experience_months = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'all_source_users_enriched'
        ordering = ('programming_languages',)

