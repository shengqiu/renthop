# 'listing_id'
- the listing ID

# '_id'
- the mongoDB ID

# 'display_address'
- the address without unit number

# 'description'
- text field, need to remove the tags

# 'created'
- date field, can be processed into year, date, hour, time

# 'price'
- float field, 

# 'bedrooms'
- float field, 

# 'interest_level'
- text field,

# 'longitude'
- float field,  around -74.0

# 'photos'
- list of String, need to be processed into number of pics

# 'manager_id'
- list of string, so this is like, building  manager..., 4399 distinct managers

# 'latitude'
- float field, around 40.0

# 'bathrooms'
- float field, 

# 'building_id'
- text field, a lot of them are 0, there are 11635 non-zero 

# 'street_address'
- text field, there are 25766, there are no unit/suite information

# 'features'
- text field, there are 2897 distinct field, but some of them can be combined
