# from typing import Annotated,Literal
# from datetime import datetime, time, timedelta
# from uuid import UUID
# from fastapi import FastAPI, Query, Body, Header
# from enum import Enum
# from app.model import UserModel
#
# from pydantic import BaseModel, Field, HttpUrl
#
#
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     googlenet = "googlenet"
#     lenet = "lenet"
#
# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title = "description" , max_length=300, examples=["A very nice item"] )
#     price: float = Field(gt=0, description="The price must be greater than 0"),
#     tax: float | None = None
#     tags: set[str] = set() #Set Example
#     reviews: list[str] = [] # List Example
#     image: Image | None = None #Nested Models Example
#     images : list[Image] | None = None #List of Nested models
#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ]
#         }
#     }
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
#     "baz": {
#         "name": "Baz",
#         "description": "There goes my baz",
#         "price": 50.2,
#         "tax": 10.5,
#     },
# }
#
# class FilterParams(BaseModel):
#     model_config = {"extra": "forbid"}
#
#     limit: int = Field(100, gt=0, le=100)
#     offset: int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at"
#     tags: list[str] = []
#
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#
#
# #Without type
# # @app.get("/items/{item_id}")
# # async def read_item(item_id):
# #     return {"item_id": item_id}
# #
# # @app.get("/items/with_type/{item_id}")
# # async def read_item(item_id: int):
# #     return {"item_id": item_id}
#
# #Skip and limit support
# @app.get("/items")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]
#
# #Optional Parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"Description": "This item is short."})
#     return item
#
# #Multiple path and query parameters¶
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: str = None, short: bool = False):
#     item = {"owner_id": user_id, "item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"Description": "This item is short."})
#
#     return item
#
# #Required  Required query parameters
# @app.get("/users/{user_id}/items/{item_id}/required")
# async def read_user_item(user_id: int, item_id: str, q: str, short: bool, skip: int = 0, limit: int | None = None):
#     item = {"owner_id": user_id, "item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"Description": "This item is short."})
#     return item
#
# @app.get("/models/{model_name}")
# async def read_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": "alexnet", "message": "Deep Learning with AlexNet"}
#     if model_name.value == "googlenet":
#         return {"model_name": "googlenet", "message": "Deep Learning with GoogleNet"}
#     return {"model_name": model_name, "message": "Some model"}
#
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}
#
#
# @app.post("/model/items")
# async def create_item(item: Item):
#     item_dic = item.dict()
#     if item.tax is not None:
#         price_with_tax = item.price + item.tax
#         item_dic.update({"price_with_tax": price_with_tax})
#     return item_dic
#
# @app.put("/model/items/{name}")
# async def update_item(name: str, item: Item, q: str | None = None):
#     result = {"name": name, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result
#
# #Use Annotated in the type for the q parameter¶
# #Annoted Query with Multiple query validation options
# #Add regular expressions
# @app.get("/model/items")
# # async def read_items(q: str | None = Query(default=None, max_length=50)):
# # async def read_items(q: Annotated[str | None, Query(max_length=50)] = None ):
# # async def read_items(q: Annotated[str, Query(max_length=50)] = None ):
# # async def read_items(q: Annotated[str, Query(min_length=5, max_length=50)] = None ):
# # async def read_items(q: Annotated[str, Query(min_length=5, max_length=50, pattern="^fixedquery$")] = None ):
# # async def read_items(q: Annotated[str, Query(min_length=5, max_length=50)] = "fixedquery" ):
# # async def read_items(q: Annotated[str, Query(min_length=5, max_length=50)]): #q is required
# # async def read_items(q: Annotated[str | None, Query(min_length=5, max_length=50)]): #q is required but None is acceptable
# # async def read_items(q: Annotated[list[str] | None, Query(min_length=5, max_length=50)]): #q is of list of str
# # async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]): #q is of list of str and set default value
# async def read_items(q: Annotated[list, Query()] = ["foo", "bar"]): #q is of list and set default value
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
# #Declare more metadata¶
# @app.get("/model/items/query")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#         ),
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
# #
# # @app.get("/path/params/items/{item_id}")
# # async def read_items_with_params(
# #     # item_id: Annotated[int, Path(title="The ID of the item to get")],
# #     *,
# #     item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)],
# #     q: Annotated[str | None, Query(alias="item-query")] = None,
# # ):
# #     results = {"item_id": item_id}
# #     if q:
# #         results.update({"q": q})
# #     return results
#
# @app.get("/query/filter/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query
#
#
#
# @app.put("/embed/items/{item_id}")
# async def update_embeded_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     item: Annotated[
#         Item,
#         Body(
#             examples=[
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 },
#                 {
#                     "name": "Bar",
#                     "price": "35.4",
#                 },
#                 {
#                     "name": "Baz",
#                     "price": "thirty five point four",
#                 }
#             ],
#         ),
#     ]
#     results = {"item_id": item_id, "item": item}
#     return results
#
#
# @app.put("/embed/items/openapi/{item_id}")
# async def update_embed_item_open_api_examples(
#     *,
#     item_id: int,
#     item: Annotated[
#         Item,
#         Body(
#             openapi_examples={
#                 "normal": {
#                     "summary": "A normal example",
#                     "description": "A **normal** item works correctly.",
#                     "value": {
#                         "name": "Foo",
#                         "description": "A very nice Item",
#                         "price": 35.4,
#                         "tax": 3.2,
#                     },
#                 },
#                 "converted": {
#                     "summary": "An example with converted data",
#                     "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
#                     "value": {
#                         "name": "Bar",
#                         "price": "35.4",
#                     },
#                 },
#                 "invalid": {
#                     "summary": "Invalid data is rejected with an error",
#                     "value": {
#                         "name": "Baz",
#                         "price": "thirty five point four",
#                     },
#                 },
#             },
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results
#
#
# @app.put("/items/with_complex_data_types/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_datetime: Annotated[datetime, Body()],
#     end_datetime: Annotated[datetime, Body()],
#     process_after: Annotated[timedelta, Body()],
#     repeat_at: Annotated[time | None, Body()] = None,
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "process_after": process_after,
#         "repeat_at": repeat_at,
#         "start_process": start_process,
#         "duration": duration,
#     }
#
#
# @app.get("/user-agent/items/")
# async def read_items(user_agent: Annotated[str | None, Header()] = None):
#     return {"User-Agent": user_agent}
#
#
# @app.get("/strange_header/items/")
# async def read_items(
#     strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
# ):
#     return {"strange_header": strange_header}
#
#
# @app.post("/response/items/")
# async def create_item(item: Item) -> Item:
#     return item
#
#
# @app.get("/response/items/")
# async def read_items() -> list[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]
#
#
#
# @app.get("/response/items/{item_id}/name", response_model=Item, response_model_exclude=["name", "description"])
# async def read_item_name(item_id : str) -> Item:
#     return items[item_id]
#
# @app.get("/response/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
# async def read_item_public_data(item_id: str):
#     return items[item_id]
#
#
# @app.post("/user/", response_model=UserModel.UserOut)
# async def create_user(user_in: UserModel.UserIn):
#     user_saved = UserModel.fake_save_user(user_in)
#     return user_saved