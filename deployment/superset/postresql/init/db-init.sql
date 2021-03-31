/*
 * Copyright (c) 2021. Members of Forome Association
 *
 * Developed by https://github.com/artazar
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *         http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

CREATE DATABASE superset;
CREATE USER superset WITH PASSWORD 'secret1';
GRANT ALL PRIVILEGES ON DATABASE "superset" to superset;
CREATE DATABASE student;
CREATE USER student WITH PASSWORD 'secret2';
GRANT ALL PRIVILEGES ON DATABASE "student" to student;
