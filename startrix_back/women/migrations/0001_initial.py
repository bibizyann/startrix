# Generated by Django 5.0.2 on 2024-03-25 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubRawCommits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.TextField(blank=True, null=True)),
                ('commited_at', models.DateTimeField(blank=True, null=True)),
                ('author_name', models.TextField(blank=True, null=True)),
                ('best_email', models.TextField(blank=True, null=True)),
                ('author_id', models.BigIntegerField(blank=True, null=True)),
                ('author_login', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'github_raw_commits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubRawReadmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.BigIntegerField(blank=True, null=True)),
                ('readme', models.TextField(blank=True, null=True)),
                ('readme_tokens', models.FloatField(blank=True, null=True)),
                ('parsed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'github_raw_readmes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubRawRepos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('default_branch', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('fork', models.BooleanField(blank=True, null=True)),
                ('forks_count', models.BigIntegerField(blank=True, null=True)),
                ('full_name', models.TextField(blank=True, null=True)),
                ('has_issues', models.BooleanField(blank=True, null=True)),
                ('has_projects', models.BooleanField(blank=True, null=True)),
                ('has_wiki', models.BooleanField(blank=True, null=True)),
                ('has_downloads', models.BooleanField(blank=True, null=True)),
                ('homepage', models.TextField(blank=True, null=True)),
                ('language', models.TextField(blank=True, null=True)),
                ('license_key', models.TextField(blank=True, null=True)),
                ('license_name', models.TextField(blank=True, null=True)),
                ('license_spdx_id', models.TextField(blank=True, null=True)),
                ('mirror_url', models.TextField(blank=True, null=True)),
                ('open_issues_count', models.BigIntegerField(blank=True, null=True)),
                ('owner_node_id', models.TextField(blank=True, null=True)),
                ('owner_id', models.BigIntegerField(blank=True, null=True)),
                ('owner_login', models.TextField(blank=True, null=True)),
                ('owner_site_admin', models.BooleanField(blank=True, null=True)),
                ('owner_type', models.TextField(blank=True, null=True)),
                ('pushed_at', models.DateTimeField(blank=True, null=True)),
                ('repo_id', models.BigIntegerField(blank=True, null=True)),
                ('node_id', models.TextField(blank=True, null=True)),
                ('size', models.BigIntegerField(blank=True, null=True)),
                ('stargazers_count', models.BigIntegerField(blank=True, null=True)),
                ('commits_count', models.FloatField(blank=True, null=True)),
                ('topics', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('watchers_count', models.BigIntegerField(blank=True, null=True)),
                ('latest_commit_date', models.DateTimeField(blank=True, null=True)),
                ('has_pages', models.BooleanField(blank=True, null=True)),
                ('parsed_at', models.DateTimeField(blank=True, null=True)),
                ('is_readme', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'github_raw_repos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubRawStars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.BigIntegerField(blank=True, null=True)),
                ('starred_at', models.DateTimeField(blank=True, null=True)),
                ('parsed_at', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('user_node_id', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'github_raw_stars',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GithubRawUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('node_id', models.TextField(blank=True, null=True)),
                ('login', models.TextField(blank=True, null=True)),
                ('avatar_url', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('site_admin', models.BooleanField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('company', models.TextField(blank=True, null=True)),
                ('blog', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('hireable', models.BooleanField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('twitter_username', models.TextField(blank=True, null=True)),
                ('public_repos', models.BigIntegerField(blank=True, null=True)),
                ('public_gists', models.BigIntegerField(blank=True, null=True)),
                ('followers', models.BigIntegerField(blank=True, null=True)),
                ('following', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('socials', models.TextField(blank=True, null=True)),
                ('parsed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'github_raw_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LinkedinRawProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn_id', models.TextField(blank=True, null=True)),
                ('profile_link', models.TextField(blank=True, null=True)),
                ('firstname', models.TextField(blank=True, db_column='firstName', null=True)),
                ('lastname', models.TextField(blank=True, db_column='lastName', null=True)),
                ('locationname', models.TextField(blank=True, db_column='locationName', null=True)),
                ('geolocationname', models.TextField(blank=True, db_column='geoLocationName', null=True)),
                ('headline', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('student', models.BooleanField(blank=True, null=True)),
                ('industryname', models.TextField(blank=True, db_column='industryName', null=True)),
                ('experiences', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('languages', models.TextField(blank=True, null=True)),
                ('parsed_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'linkedin_raw_profiles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LinkedinRawSearchPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urn_id', models.TextField(blank=True, null=True)),
                ('jobtitle', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('parsed_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'linkedin_raw_search_people',
                'managed': False,
            },
        ),
    ]
