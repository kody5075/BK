// SPDX-License-Identifier: MIT

pragma solidity ^0.8.11;

contract MyContract {


    string[] public row;

    function getRow() public view returns (string[] memory) {
        return row;
    }

    function pushToRow(string memory newValue) public {
        row.push(newValue);
    }


}