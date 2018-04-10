#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""add uid field index to task instance

Revision ID: e7a93f4cb5c8
Revises: d02246ccf39b
Create Date: 2018-04-10 00:14:16.600752

"""

# revision identifiers, used by Alembic.
revision = 'e7a93f4cb5c8'
down_revision = 'd02246ccf39b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index('ti_uid', 'task_instance', ['uid'], unique=False)


def downgrade():
    op.drop_index('ti_uid', table_name='task_instance')
