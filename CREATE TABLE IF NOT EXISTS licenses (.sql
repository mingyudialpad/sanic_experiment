CREATE TABLE IF NOT EXISTS licenses (
  id varchar(10) NOT NULL,
  liness varchar(10),
  lite_lines varchar(10),
  agents varchar(10),
  magenta_lines varchar(10),
  tollfree_room_lines varchar(10),
  group_lines varchar(10),
  tollfree_group_lines varchar(10),
  fax_lines varchar(10),
  uc_tier_1 varchar(10),
  uc_tollfree_tier_1 varchar(10),
  tollfree_tier_b varchar(10),
  tollfree_tier_c varchar(10),
  tollfree_tier_d varchar(10),
  local_presence_top100 varchar(10),
  local_presence_all varchar(10),
  PRIMARY KEY (id)
)

INSERT INTO
  licenses (
    id,
    liness,
    lite_lines,
    agents,
    magenta_lines,
    tollfree_room_lines,
    group_lines,
    tollfree_group_lines,
    fax_lines,
    uc_tier_1,
    uc_tollfree_tier_1,
    tollfree_tier_b,
    tollfree_tier_c,
    tollfree_tier_d,
    local_presence_top100,
    local_presence_all
  )
VALUES
  (
    '1',
    '1.12',
    '1.13',
    '1.14',
    '1.15',
    '1.16',
    '1.17',
    '1.18',
    '1.19',
    '1.20',
    '1.21',
    '1.22',
    '1.23',
    '1.24',
    '1.25',
    '1.26'
  );
