# Generated by Django 2.2.1 on 2019-05-19 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ActiveAdminComment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("namespace", models.CharField(blank=True, max_length=256, null=True)),
                ("body", models.TextField(blank=True, null=True)),
                (
                    "resource_type",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("resource_id", models.IntegerField(blank=True, null=True)),
                (
                    "author_type",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("author_id", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "active_admin_comments", "managed": False},
        ),
        migrations.CreateModel(
            name="AdminUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=256, unique=True)),
                ("encrypted_password", models.CharField(max_length=256)),
                (
                    "reset_password_token",
                    models.CharField(
                        blank=True, max_length=256, null=True, unique=True
                    ),
                ),
                ("reset_password_sent_at", models.DateTimeField(blank=True, null=True)),
                ("remember_created_at", models.DateTimeField(blank=True, null=True)),
                ("sign_in_count", models.IntegerField()),
                ("current_sign_in_at", models.DateTimeField(blank=True, null=True)),
                ("last_sign_in_at", models.DateTimeField(blank=True, null=True)),
                (
                    "current_sign_in_ip",
                    models.GenericIPAddressField(blank=True, null=True),
                ),
                (
                    "last_sign_in_ip",
                    models.GenericIPAddressField(blank=True, null=True),
                ),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("role_id", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "admin_users", "managed": False},
        ),
        migrations.CreateModel(
            name="ArInternalMetadata",
            fields=[
                (
                    "key",
                    models.CharField(max_length=256, primary_key=True, serialize=False),
                ),
                ("value", models.CharField(blank=True, max_length=256, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "ar_internal_metadata", "managed": False},
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("url", models.CharField(blank=True, max_length=256, null=True)),
                ("start_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                ("address1", models.CharField(blank=True, max_length=256, null=True)),
                ("address2", models.CharField(blank=True, max_length=256, null=True)),
                ("city", models.CharField(blank=True, max_length=256, null=True)),
                ("state", models.CharField(blank=True, max_length=256, null=True)),
                ("zip", models.CharField(blank=True, max_length=256, null=True)),
                ("scholarship_available", models.BooleanField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("source_id", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "source_type",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("source_updated", models.DateTimeField(blank=True, null=True)),
                ("group", models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={"db_table": "events", "managed": False},
        ),
        migrations.CreateModel(
            name="GitHubStatistic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("source_id", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "source_type",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("state", models.CharField(blank=True, max_length=256, null=True)),
                ("additions", models.IntegerField(blank=True, null=True)),
                ("deletions", models.IntegerField(blank=True, null=True)),
                ("repository", models.CharField(blank=True, max_length=256, null=True)),
                ("url", models.CharField(blank=True, max_length=256, null=True)),
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("number", models.CharField(blank=True, max_length=256, null=True)),
                ("completed_on", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "git_hub_statistics", "managed": False},
        ),
        migrations.CreateModel(
            name="GitHubUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(blank=True, null=True)),
                (
                    "git_hub_login",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("avatar_url", models.CharField(blank=True, max_length=256, null=True)),
                ("api_url", models.CharField(blank=True, max_length=256, null=True)),
                ("html_url", models.CharField(blank=True, max_length=256, null=True)),
                ("git_hub_id", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "git_hub_users", "managed": False},
        ),
        migrations.CreateModel(
            name="OldCodeSchool",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("url", models.CharField(blank=True, max_length=256, null=True)),
                ("logo", models.CharField(blank=True, max_length=256, null=True)),
                ("full_time", models.BooleanField(blank=True, null=True)),
                ("hardware_included", models.BooleanField(blank=True, null=True)),
                ("has_online", models.BooleanField(blank=True, null=True)),
                ("online_only", models.BooleanField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("notes", models.TextField(blank=True, null=True)),
                ("mooc", models.BooleanField()),
                ("is_partner", models.BooleanField()),
                ("rep_name", models.CharField(blank=True, max_length=256, null=True)),
                ("rep_email", models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={"db_table": "code_schools", "managed": False},
        ),
        migrations.CreateModel(
            name="OldLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("va_accepted", models.BooleanField(blank=True, null=True)),
                ("address1", models.CharField(blank=True, max_length=256, null=True)),
                ("address2", models.CharField(blank=True, max_length=256, null=True)),
                ("city", models.CharField(blank=True, max_length=256, null=True)),
                ("state", models.CharField(blank=True, max_length=256, null=True)),
                ("zip", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "locations", "managed": False},
        ),
        migrations.CreateModel(
            name="OldTeamMember",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("role", models.CharField(blank=True, max_length=256, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("description", models.TextField(blank=True, null=True)),
                ("group", models.CharField(blank=True, max_length=256, null=True)),
                ("image_src", models.CharField(blank=True, max_length=256, null=True)),
                ("email", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={"db_table": "team_members", "managed": False},
        ),
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("service_id", models.IntegerField(blank=True, null=True)),
                ("language", models.CharField(blank=True, max_length=256, null=True)),
                ("details", models.TextField(blank=True, null=True)),
                ("assigned_mentor_id", models.IntegerField(blank=True, null=True)),
                ("requested_mentor_id", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("status", models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={"db_table": "requests", "managed": False},
        ),
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("url", models.CharField(blank=True, max_length=256, null=True)),
                ("category", models.CharField(blank=True, max_length=256, null=True)),
                ("language", models.CharField(blank=True, max_length=256, null=True)),
                ("paid", models.BooleanField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                ("votes_count", models.IntegerField()),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "resources", "managed": False},
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "roles", "managed": False},
        ),
        migrations.CreateModel(
            name="SchemaMigration",
            fields=[
                (
                    "version",
                    models.CharField(max_length=256, primary_key=True, serialize=False),
                )
            ],
            options={"db_table": "schema_migrations", "managed": False},
        ),
        migrations.CreateModel(
            name="Scholarship",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=256, null=True)),
                ("terms", models.TextField(blank=True, null=True)),
                ("open_time", models.DateTimeField(blank=True, null=True)),
                ("close_time", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "scholarships", "managed": False},
        ),
        migrations.CreateModel(
            name="ScholarshipApplication",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reason", models.TextField(blank=True, null=True)),
                ("terms_accepted", models.BooleanField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "scholarship_applications", "managed": False},
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "services", "managed": False},
        ),
        migrations.CreateModel(
            name="SlackUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slack_id", models.CharField(blank=True, max_length=256, null=True)),
                ("slack_name", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "slack_real_name",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "slack_display_name",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "slack_email",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("user_id", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "slack_users", "managed": False},
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=256, null=True, unique=True
                    ),
                ),
                ("taggings_count", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "tags", "managed": False},
        ),
        migrations.CreateModel(
            name="Tagging",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_id", models.IntegerField(blank=True, null=True)),
                (
                    "taggable_type",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("taggable_id", models.IntegerField(blank=True, null=True)),
                (
                    "tagger_type",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("tagger_id", models.IntegerField(blank=True, null=True)),
                ("context", models.CharField(blank=True, max_length=128, null=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "taggings", "managed": False},
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "votes", "managed": False},
        ),
        migrations.CreateModel(
            name="CodeSchool",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("url", models.CharField(blank=True, max_length=256, null=True)),
                ("logo", models.CharField(blank=True, max_length=256, null=True)),
                ("full_time", models.BooleanField(blank=True, null=True)),
                ("hardware_included", models.BooleanField(blank=True, null=True)),
                ("has_online", models.BooleanField(blank=True, null=True)),
                ("online_only", models.BooleanField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("notes", models.TextField(blank=True, null=True)),
                ("mooc", models.BooleanField()),
                ("is_partner", models.BooleanField()),
                ("rep_name", models.CharField(blank=True, max_length=256, null=True)),
                ("rep_email", models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={"db_table": "api_code_schools"},
        ),
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("role", models.CharField(blank=True, max_length=256, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("description", models.TextField(blank=True, null=True)),
                ("group", models.CharField(blank=True, max_length=256, null=True)),
                ("image_src", models.CharField(blank=True, max_length=256, null=True)),
                ("email", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={"db_table": "api_team_members"},
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("va_accepted", models.BooleanField(blank=True, null=True)),
                ("address1", models.CharField(blank=True, max_length=256, null=True)),
                ("address2", models.CharField(blank=True, max_length=256, null=True)),
                ("city", models.CharField(blank=True, max_length=256, null=True)),
                ("state", models.CharField(blank=True, max_length=256, null=True)),
                ("zip", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                (
                    "code_school",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="locations",
                        to="api.CodeSchool",
                    ),
                ),
            ],
            options={"db_table": "api_locations"},
        ),
    ]
