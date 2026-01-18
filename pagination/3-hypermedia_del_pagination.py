#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination info based on index
        robust to deleted rows
        """
        dataset = self.indexed_dataset()
        assert index is None or (index >= 0 and index <= max(dataset.keys()))

        if index is None:
            index = 0

        data = []
        current_idx = index
        count = 0

        while count < page_size and current_idx <= max(dataset.keys()):
            if current_idx in dataset:
                data.append(dataset[current_idx])
                count += 1
            current_idx += 1

        next_index = current_idx if current_idx <= max(dataset.keys()) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
