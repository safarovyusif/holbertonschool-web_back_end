#!/usr/bin/env python3
"""
Hypermedia pagination implementation
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset (list of rows)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range_idxs = index_range(page, page_size)
        start_idx = range_idxs[0]
        end_idx = range_idxs[1]

        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary containing hypermedia pagination data
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
