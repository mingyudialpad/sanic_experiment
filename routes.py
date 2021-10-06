from sanic.response import json

from project.tables import pricing


def setup_routes(app):
    @app.route("/pricing")
    async def book_list(request):
        query = pricing.select()
        rows = await request.app.db.fetch_all(query)
        return json({
            'pricing': [{row['id']: row['lite_lines']} for row in rows]
        })
