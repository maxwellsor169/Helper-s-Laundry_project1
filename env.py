import os


os.environ.setdefault(
    "DATABASE_URL", "postgresql://neondb_owner:npg_SUfrVz6NsP8k@ep-flat-thunder-a28il97g.eu-central-1.aws.neon.tech/crepe_pulp_exact_584902"
)
os.environ.setdefault(
    "SECRET_KEY", "Max1%2@3~*wel)l"
)
os.environ["DEVELOPMENT"] = 'True'
