#  Copyright (c) 2021. Members of Forome Association
#
#  Developed by https://github.com/artazar
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os

from cachelib import RedisCache

MAPBOX_COURSE_KEY = 'pk.eyJ1IjoibW1jZW50cmUiLCJhIjoiY2ttd3I3d2lhMDgyODJvcTlzZnQ3bTJsayJ9.Lc_Y2ZtmhmcKZIMG-UWY6Q'
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', MAPBOX_COURSE_KEY)
POSTGRES_HOST = os.getenv('POSTGRES_HOST', "postgres")
CACHE_CONFIG = {
	'CACHE_TYPE': 'redis',
	'CACHE_DEFAULT_TIMEOUT': 300,
	'CACHE_KEY_PREFIX': 'superset_',
	'CACHE_REDIS_HOST': 'redis',
	'CACHE_REDIS_PORT': 6379,
	'CACHE_REDIS_DB': 1,
	'CACHE_REDIS_URL': 'redis://redis:6379/1'}

SQLALCHEMY_DATABASE_URI = \
	'postgresql+psycopg2://superset:secret1@{}:5432/superset'\
		.format(POSTGRES_HOST)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'

class CeleryConfig(object):
	BROKER_URL = 'redis://redis:6379/0'
	CELERY_IMPORTS = ('superset.sql_lab', )
	CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
	CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

CELERY_CONFIG = CeleryConfig
RESULTS_BACKEND = RedisCache(
	host='redis',
	port=6379,
	key_prefix='superset_results'
)
