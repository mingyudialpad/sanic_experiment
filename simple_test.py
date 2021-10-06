from sanic import Sanic
from sanic import response
from sanic.log import logger
from controller import my_bp
from sanic.response import text
from sanic.response import json
from databases import Database
from tables import pricing
  
app = Sanic("My First Sanic App")

app.ctx.db = Database('postgresql://postgres:postgres@localhost/postgres')

@app.listener('after_server_stop')
async def disconnect_from_db(*args, **kwargs):
    await app.ctx.db.disconnect()

@app.listener('after_server_start')
async def initdb(*args, **kwargs):
    await app.ctx.db.connect()

# registering route defined by blueprint
app.blueprint(my_bp)
  
# webapp path defined used 'route' decorator
@app.route("/")
def run(request):
    return response.text("Hello World !")
  

@app.route("/licenses")
async def price_list(request):
    return text("ok")

@app.get('/licenses/<plan_id>')
async def handler(request, plan_id):
    query = "SELECT * FROM licenses WHERE id = :plan_id"
    result = await request.app.ctx.db.fetch_one(query=query, values={"id": plan_id})
    return text(result)

@app.delete('/licenses/<plan_id>')
async def handler(request, plan_id):
    query = "DELETE * FROM licenses WHERE id = :plan_id"
    result = await request.app.ctx.db.fetch_one(query=query, values={"id": plan_id})
    return text(result)

@app.put('/licenses/<plan_id>')
async def handler(request, plan_id):
    query = pricing.insert()
    values = [
        {"id": "1", 'liness': "1.22", "lite_lines": "1.23", "agents": "1.24",  "lite_support_agents": "1.25"  ,"magenta_lines":"1.26",  "tollfree_room_lines": "1.27",  "uc_tier_1":"1.28", "uc_tollfree_tier_1":"1.29",  "tollfree_tier_b":"1.210"},
    ]
    await request.app.ctx.db.execute_many(query=query, values=values)

@app.post('/licenses')
async def handler(request):
    query = pricing.insert()
    values = [
        {"id": "2", 'liness': "2.22", "lite_lines": "2.23", "agents": "2.24",  "lite_support_agents": "2.25"  ,"magenta_lines":"2.26",  "tollfree_room_lines": "2.27",  "uc_tier_1":"2.28", "uc_tollfree_tier_1":"2.29",  "tollfree_tier_b":"2.210"},
        {"id": "3", 'liness': "3.22", "lite_lines": "3.23", "agents": "3.24",  "lite_support_agents": "3.25"  ,"magenta_lines":"3.26",  "tollfree_room_lines": "3.27",  "uc_tier_1":"3.28", "uc_tollfree_tier_1":"3.29",  "tollfree_tier_b":"3.210"},
    ]
    await request.app.ctx.db.execute_many(query=query, values=values)

  
app.run(host ="0.0.0.0", port = 8000, debug = True)