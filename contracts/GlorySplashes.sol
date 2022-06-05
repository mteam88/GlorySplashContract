// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

import '@openzeppelin/contracts/token/ERC1155/ERC1155.sol';
import "@openzeppelin/contracts/utils/Strings.sol";
import "hardhat/console.sol";

contract GlorySplashes is ERC1155 {
    uint256 public constant MAXID=14;

    constructor() ERC1155("ipfs://QmWQYDLsNQh7PuT4bNUvYHgSoF3bbQMUALDhQcvGViy968/{id}.json") {
        for (uint256 i=0; i<15; i++) {
        _mint(msg.sender, i, 1, "");
        }
    }

    function uri(uint256 _tokenId) override public view returns (string memory) {
        return string(
            abi.encodePacked(
                "ipfs://QmWQYDLsNQh7PuT4bNUvYHgSoF3bbQMUALDhQcvGViy968/",
                Strings.toString(_tokenId),
                ".json"
            )
        );
    }
}