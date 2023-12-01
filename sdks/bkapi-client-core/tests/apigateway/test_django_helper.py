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
import pytest

from bkapi_client_core.apigateway import django_helper


@pytest.mark.parametrize(
    ("endpoint", "bk_api_url_tmpl", "expected"),
    [
        ("http://example.com", "http://", "http://example.com"),
        (None, "http://{api_name}.example.com", "http://{api_name}.example.com"),
        (None, "http://{gateway_name}.example.com", "http://{gateway_name}.example.com"),
        (None, "http://{bkapi_api_name}.example.com", "http://{bkapi_api_name}.example.com"),
        (None, "http://{test}.example.com", "http://{test}.example.com"),
        (None, "", ""),
    ],
)
def test_get_endpoint(mocker, endpoint, bk_api_url_tmpl, expected):
    settings = mocker.patch.object(django_helper, "settings")
    settings.get.return_value = bk_api_url_tmpl

    assert django_helper._get_endpoint(endpoint) == expected
