# -*- coding: utf-8 -*-
"""
 * TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-蓝鲸 PaaS 平台(BlueKing-PaaS) available.
 * Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
 * Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://opensource.org/licenses/MIT
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 * an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
"""


def pytest_configure():
    from django.conf import settings

    MIDDLEWARE = []

    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        SECRET_KEY='not very secret in tests',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
            },
        ],
        USE_TZ=True,
        TIME_ZONE='Asia/Shanghai',
        MIDDLEWARE=MIDDLEWARE,
        MIDDLEWARE_CLASSES=MIDDLEWARE,
        INSTALLED_APPS=(
            'bkstorages',
            'tests',
        ),
        # DEFAULT_FILE_STORAGE = 'bkstorages.backends.rgw.RGWBoto3Storage',
        # RGW settings
        RGW_AUTO_CREATE_BUCKET=False,
        RGW_ENDPOINT_URL='http://localhost/',
        RGW_ACCESS_KEY_ID="minio",
        RGW_SECRET_ACCESS_KEY="",
        RGW_STORAGE_BUCKET_NAME="unittest",
        RGW_REGION_NAME="us-east-1",
        # BK_REPO
        BKREPO_ENDPOINT_URL="",
        BKREPO_USERNAME="",
        BKREPO_PASSWORD="",
        BKREPO_PROJECT="",
        BKREPO_BUCKET="",
    )

    try:
        import django

        django.setup()
    except AttributeError:
        pass
