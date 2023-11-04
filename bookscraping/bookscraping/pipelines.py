from itemadapter import ItemAdapter


class BookscrapingPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Strip all white spaces from string
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != "description":
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()

        # Convert 'category' and 'product' to lowercase
        lower_case_keys = ["category", "product"]
        for lower_case_key in lower_case_keys:
            value = adapter.get(lower_case_key)
            adapter[lower_case_key] = value.lower()

        # Convert 'num_reviews' string to a number
        num_reviews_string = adapter.get("num_reviews")
        adapter['num_reviews'] = int(num_reviews_string)

        return item
