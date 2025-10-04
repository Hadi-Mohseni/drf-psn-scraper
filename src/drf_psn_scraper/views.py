from rest_framework.decorators import api_view
from playstation_store_scraper import scraper
from rest_framework.request import Request
from drf_psn_scraper.serializers import GameCardSerializer, GameSerializer
from rest_framework.response import Response


@api_view(["GET"])
def list_games(request: Request):
    params = request.query_params
    page = params["page"] if "page" in params else 1
    region = params["region"] if "region" in params else "en-us"
    region = scraper.REGION(region)
    games, page, last_page = scraper.list_games(region, page)
    serializer = GameCardSerializer(games, many=True)
    return Response(
        {
            "games": serializer.data,
            "currentPage": page,
            "lastPage": last_page,
        },
        200,
    )


@api_view(["GET"])
def retrieve_game(request: Request, id):
    params = request.query_params
    region = params["region"] if "region" in params else "en-us"
    region = scraper.REGION(region)
    result = scraper.retrieve_game(id, region)
    serializer = GameSerializer(result)
    return Response(serializer.data, 200)
